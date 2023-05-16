import mysql.connector
import os
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from app import app
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app.forms import ApplicationForm, ResumeForm
from flask_mail import Message
from app import mail 
from io import BytesIO
import time
from datetime import timedelta
from app.ai import cluster_files
from functools import wraps
from math import ceil

# MySQL database configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'jobListings',
    }
resume_folder= 'C:/Users/Shanice/Documents/COMP3901-Project/COMP3901-Project/resume_files'
job_folder= 'C:/Users/Shanice/Documents/COMP3901-Project/COMP3901-Project/job_desc_files'
# Admin Login Required Decorator
def admin_login_required(func):
    def wrapper(*args, **kwargs):
        # Check if user is authenticated and an admin
        if request.args.get('admin') == 'true':
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('ID') is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
# Define a route to display the content from the database on the webpage
@app.route('/joblisting.html', methods=['GET', 'POST'])
@login_required
def joblisting():
    # Handle search form submission
    

    # Connect to the database
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    # Retrieve the page number from the query parameters
    page = int(request.args.get('page', 1))

    # Calculate the offset
    offset = (page - 1) * 10

    if request.method == 'POST':
        search_term = request.form['search']
        query = f"SELECT jobID,jobTitle, employer, DatePosted, status FROM jobs WHERE jobTitle LIKE '%{search_term}%' LIMIT 10 OFFSET {offset}"
        cursor.execute(query)
        data = cursor.fetchall()
    else:
        # Execute a SELECT statement to retrieve all data from the database
        query = f"SELECT jobID,jobTitle, employer, DatePosted, status FROM jobs LIMIT 10 OFFSET {offset}"
        cursor.execute(query)
        data = cursor.fetchall()
    
    # Calculate the total number of jobs
    q = f"SELECT COUNT(*) FROM jobs"
    cursor.execute(q)
    total_jobs = cursor.fetchone()[0]
    
    # Calculate the total number of pages
    total_pages = ceil(total_jobs / 10)
    
    is_admin = session['admin'] == 1
    print(session['admin'])
    
    # Render the template and pass the data to the template
    return render_template('joblisting.html', data=data, is_admin=is_admin, current_page=page, total_pages=total_pages )


@app.route('/job/<int:job_id>')
def job_details(job_id):
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    query = "SELECT jobTitle, employer, DatePosted, status, jobDescription FROM jobs WHERE jobID = %s"
    cursor.execute(query, (job_id,))
    data = cursor.fetchone()
    is_admin = session['admin'] == 1
    return render_template('jobdetails.html', jobTitle=data[0], employer=data[1], DatePosted=data[2], status=data[3], jobDescription=data[4], job_id=job_id, is_admin=is_admin)


@app.route('/add_job', methods=['GET'])
def add_job():
    session.clear()
    return render_template('add_job.html')

@app.route('/application/submit/<int:job_id>', methods=['GET', 'POST'])
def submit_application(job_id):
    form = ApplicationForm()
    if form.validate_on_submit():
        # Save the uploaded files
        resume = form.resume.data
        cover_letter = form.cover_letter.data
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        cursor.execute('SELECT * FROM jobs WHERE jobID = %s', (job_id,))
        job = cursor.fetchone()
        cursor.close()
        print(job[5])
        # Send the application as an email
        message = Message('New Job Application', recipients=[job[5]])
        message.body = f"""
            First Name: {form.first_name.data}
            Last Name: {form.last_name.data}
            Address: {form.address.data}
            Email: {form.email.data}
            Phone Number: {form.phone_number.data}
            Position Applying For: {form.position_applying_for.data}
        """

        # Encode the file data as bytes
        resume_bytes = resume.read()
        cover_letter_bytes = cover_letter.read()

        # Attach the files to the message
        message.attach(resume.filename, 'resume/pdf', BytesIO(resume_bytes).getvalue())
        message.attach(cover_letter.filename, 'coverletter/pdf', BytesIO(cover_letter_bytes).getvalue())
        mail.send(message)

        flash('Application Submitted', 'success')
        return redirect(url_for('joblisting'))

    return render_template('application.html', form=form, job_id=job_id)


@app.route('/add_job', methods=['POST'])
def add_job_post():

    # Connect to the database
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    jobTitle = request.form['jobTitle']
    employer = request.form['employer']
    jobDescription = request.form['jobDescription']
    status = request.form['status']
    email = request.form['email']
    DatePosted = request.form['DatePosted']

    # Get the highest existing job ID from the database
    cursor.execute("SELECT MAX(jobID) FROM jobs")
    result = cursor.fetchone()
    highest_id = result[0] if result[0] else 0

    # Insert the new job into the database with the correct ID
    query = "INSERT INTO jobs (jobID, jobTitle, employer, jobDescription, status, email, DatePosted) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (highest_id + 1, jobTitle, employer, jobDescription, status, email, DatePosted)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()
    flash('Job added', 'Success')
    return redirect(url_for('joblisting'))

@app.route('/editjob/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id):
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    cursor.execute('SELECT * FROM jobs WHERE jobID = %s', (job_id,))
    job = cursor.fetchone()
    cursor.close()
    
    if job is None:
        return 'Job not found', 404
    
    if request.method == 'POST':
        jobTitle = request.form['jobTitle']
        employer = request.form['employer']
        datePosted = request.form['datePosted']
        status = request.form['status']
        jobDescription = request.form['jobDescription']
        
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        cursor.execute('UPDATE jobs SET jobTitle=%s, employer=%s, DatePosted=%s, status=%s, jobDescription=%s WHERE jobID=%s', (jobTitle, employer, datePosted, status, jobDescription, job_id))
        db.commit()
        cursor.close()
        flash('Job Edited', 'success')
        
        return redirect(url_for('job_details', job_id=job_id))
    
    return render_template('editjob.html', job_id=job_id, jobTitle=job[1], employer=job[2], DatePosted=job[3], status=job[4], jobDescription=job[6])


@app.route('/deletejob/<int:job_id>',methods=['POST','GET'])
def delete_job(job_id):

    # Connect to the database
    db = mysql.connector.connect(user='root', password= '', host= 'localhost',database= 'jobListings')
    cursor = db.cursor()
    query = "DELETE FROM jobs WHERE jobID = %s"
    values = (job_id,)
    cursor.execute(query, values)
    db.commit()
    flash('Job Deleted', 'success')
    return redirect(url_for('joblisting'))


@app.route('/', methods=['GET'])
def homepage():
    return render_template('home.html')

@app.route('/about.html', methods=['GET'])
def aboutpage():
    return render_template('about.html')

@app.route('/cardev.html', methods=['GET'])
def cardev():
    return render_template('cardev.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@app.route('/check')
def checklogin():
    if 'username' in session:
        return 'You are already logged in as ' + session['username']
    else:
        return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['ID']
        password = request.form['password']
        remember_me = request.form.get('remember')

        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['ID'] = username
            session['admin']= user[3]
            if remember_me:
                session.permanent = True
            flash('Logged in successfully', 'success')
            return redirect(url_for('joblisting'))
        else:
            flash('Invalid username or password. Please try again','error')
  
            return render_template('login.html')

    else:
        return render_template('login.html')



def loadFile():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    # Create directory for job description files
    if not os.path.exists('job_desc_files'):
        os.makedirs('job_desc_files')

    # Fetch all columns from the jobs table
    cursor.execute('SELECT * FROM `jobs`')
    data = cursor.fetchall()

    # Write job description data to individual files
    for row in data:
        job_id = str(row[0])
        job_desc = str(row).strip()

        file_name = f"{job_id}.txt"
        file_path = os.path.join('job_desc_files', file_name)

        with open(file_path, 'w+') as f:
            f.write(job_desc)


@app.route('/save_resume', methods=['GET', 'POST'])
@login_required
def save_resume():
  
    form = ResumeForm()
    if form.validate_on_submit():
        resume_file = form.resume.data
        if resume_file:
            filename = resume_file.filename
            resume_file.save(os.path.join(resume_folder, filename))
            # save the filename to the database
            db = mysql.connector.connect(**db_config)
            cursor = db.cursor()
            current_user = session['ID']
            print(current_user)
            query = f"UPDATE users SET resume = '{filename}' WHERE username = '{current_user}'"
            cursor.execute(query)
            db.commit()
            flash('Resume saved successfully!', 'success')
            return redirect(url_for('clustered_jobs'))
    else:
        print(form.errors)
    return render_template('resume.html', title='Save Resume', form=form)


@app.route('/clustered_jobs')
@login_required
def clustered_jobs():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    form = ResumeForm()
    current_user = session['ID']
    query = f"SELECT resume FROM users WHERE username = '{current_user}'"
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)
    if result[0] is None:
        # User doesn't have a resume
        return render_template('resume.html',form=form, message='You do not have a resume.')
    else:
        resume_file_name = result[0]
        loadFile()
        clustered_files = cluster_files(job_folder,resume_folder, resume_file_name)

        job_ids = []
        for file_name in clustered_files:
            if file_name == resume_file_name:
                continue
            job_id = int(os.path.splitext(file_name)[0])
            job_ids.append(job_id)

        if len(job_ids) == 0:
            # No jobs matched with the resume
            job_query = "SELECT * FROM jobs"
            cursor.execute(job_query)
            jobs = cursor.fetchall()
            return render_template('resume.html',jobs=jobs,form=form, message='Your resume did not match with any jobs.')

        else:
            job_query = f"SELECT * FROM jobs WHERE jobID IN ({','.join(str(id) for id in job_ids)})"
            cursor.execute(job_query)
            jobs = cursor.fetchall()

        
        

        return render_template('resume.html',form=form, jobs=jobs)


@app.route('/logout')
def logout():
    session.clear()  # Remove the 'name' key from the session
    flash('You have been logged out.', 'success')
    return redirect(url_for('homepage'))

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')
