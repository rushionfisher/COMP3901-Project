import mysql.connector
import os
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from app import app
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app.forms import ApplicationForm
from flask_mail import Message
from app import mail 
from io import BytesIO
import time
from datetime import timedelta
import bcrypt


# MySQL database configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'jobListings',
    }
# Define a route to display the content from the database on the webpage
@app.route('/joblisting.html', methods=['GET', 'POST'])
def joblisting():
    # Handle search form submission
    

    # Connect to the database
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    if request.method == 'POST':
        search_term = request.form['search']
        query = f"SELECT jobID,jobTitle, employer, DatePosted, status FROM jobs WHERE jobTitle LIKE '%{search_term}%'"
        cursor.execute(query)
        data = cursor.fetchall()
    else:
        # Execute a SELECT statement to retrieve all data from the database
        query = "SELECT jobID,jobTitle, employer, DatePosted, status FROM jobs"
        cursor.execute(query)
        data = cursor.fetchall()
    is_admin = 'true'
    # Render the template and pass the data to the template
    return render_template('joblisting.html', data=data, is_admin=is_admin )


@app.route('/job/<int:job_id>')
def job_details(job_id):
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    query = "SELECT jobTitle, employer, DatePosted, status, jobDescription FROM jobs WHERE jobID = %s"
    cursor.execute(query, (job_id,))
    data = cursor.fetchone()
    is_admin = 'true'
    return render_template('jobdetails.html', jobTitle=data[0], employer=data[1], DatePosted=data[2], status=data[3], jobDescription=data[4], job_id=job_id, is_admin=is_admin)


@app.route('/add_job', methods=['GET'])
def add_job():
    session.clear()
    return render_template('add_job.html')

@app.route('/application/submit', methods=['GET', 'POST'])
def submit_application():
    form = ApplicationForm()
    if form.validate_on_submit():
        # Save the uploaded files
        resume = form.resume.data
        cover_letter = form.cover_letter.data

        # Send the application as an email
        message = Message('New Job Application', recipients=['hr@example.com'])
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

    return render_template('application.html', form=form)


@app.route('/add_job', methods=['POST'])
def add_job_post():
    db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'jobListings',
    }

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
    time.sleep(3)
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
        
        return redirect(url_for('job_details', job_id=job_id))
    
    return render_template('editjob.html', job_id=job_id, jobTitle=job[1], employer=job[2], DatePosted=job[3], status=job[4], jobDescription=job[5])


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

@app.route('/staff.html', methods=['GET'])
def staff():
    return render_template('staff.html')


@app.route('/check')
def checklogin():
    if 'username' in session:
        return 'You are already logged in as ' + session['username']
    else:
        return render_template('home.html')
      
@app.route('/login', methods=['GET', 'POST'])
def login():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    if request.method == 'POST':
        # Get form data
        username = request.form['ID']
        password = request.form['password']
        remember_me = request.form.get('remember')

        # Validate input
        if not username or not password:
            error = 'Username and password are required'
            return render_template('login.html', error=error)

        # Retrieve user data from database
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        data = cursor.fetchone()

        if not data:
            error = 'Invalid login'
            return render_template('login.html', error=error)

        # Check password
        stored_hash = data[2]
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
            # Login successful
            session['username'] = username
            if remember_me:
                session.permanent = True  
            message = "Login Successful"
            return render_template('login.html', message=message)
        else:
            # Login unsuccessful
            error = 'Invalid login'
            return render_template('login.html', error=error)

    return render_template('login.html')

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')