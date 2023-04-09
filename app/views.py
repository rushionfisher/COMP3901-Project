from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
import mysql.connector
from app import app


# MySQL database configuration

# Define a route to display the content from the database on the webpage
@app.route('/joblisting.html', methods=['GET', 'POST'])
def joblisting():
    # Handle search form submission
    db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'jobListings',
    }

    # Connect to the database
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()

    if request.method == 'POST':
        search_term = request.form['search']
        query = f"SELECT jobTitle, employer, DatePosted, status FROM jobs WHERE jobTitle LIKE '%{search_term}%'"
        cursor.execute(query)
        data = cursor.fetchall()
    else:
        # Execute a SELECT statement to retrieve all data from the database
        query = "SELECT jobTitle, employer, DatePosted, status FROM jobs"
        cursor.execute(query)
        data = cursor.fetchall()
    is_admin = 'true'
    # Render the template and pass the data to the template
    return render_template('joblisting.html', data=data, is_admin=is_admin )

@app.route('/add_job', methods=['GET'])
def add_job():
    return render_template('add_job.html')

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
    return redirect(url_for('joblisting'))

@app.route('/', methods=['GET'])
def homepage():
    return render_template('home.html')

@app.route('/about.html', methods=['GET'])
def aboutpage():
    return render_template('about.html')



