"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from app import app 
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app.forms import ApplicationForm
from flask_mail import Message
from app import mail 
from io import BytesIO





###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

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
        message.attach(resume.filename, 'application/pdf', BytesIO(resume_bytes).getvalue())
        message.attach(cover_letter.filename, 'application/pdf', BytesIO(cover_letter_bytes).getvalue())
        mail.send(message)

        flash('Property added successfully', 'success')

    return render_template('application.html', form=form)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
