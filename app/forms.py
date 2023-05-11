from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, Length


class ApplicationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    address = TextAreaField('Address', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    position_applying_for = TextAreaField('Position Applying For', validators=[DataRequired(), Length(max=50)])
    resume = FileField('Upload Resume', validators=[DataRequired()])
    cover_letter = FileField('Upload Cover Letter', validators=[DataRequired()])
    submit = SubmitField('Submit Application')

class ResumeForm(FlaskForm):
    resume = FileField('Upload Resume Here', validators=[DataRequired()])
    save = SubmitField('Save Resume')
