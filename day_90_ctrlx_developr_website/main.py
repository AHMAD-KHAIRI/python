import requests, os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TelField, SelectMultipleField, widgets, BooleanField
from wtforms.validators import DataRequired, Email, InputRequired
from markupsafe import Markup
from dotenv import load_dotenv
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "some secret string"
Bootstrap5(app)


class BootstrapListWidget(widgets.ListWidget):
     
    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        html = [f"<{self.html_tag} {widgets.html_params(**kwargs)}>"]
        for subfield in field:
            if self.prefix_label:
                html.append(f"<li class='list-group-item'>{subfield.label} {subfield(class_='form-check-input ms-1')}</li>")
            else:
                html.append(f"<li class='list-group-item'>{subfield(class_='form-check-input me-1')} {subfield.label}</li>")
        html.append("</%s>" % self.html_tag)
        return Markup("".join(html))

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class RegistrationForm(FlaskForm):
    group_member_one = StringField(label='Group member one: Enter your name', validators=[DataRequired(message="This field is required.")])
    group_member_two = StringField(label='Group member two: Enter your name')
    group_member_three = StringField(label='Group member three: Enter your name')
    group_member_four = StringField(label='Group member four: Enter your name')

    sector_categories = MultiCheckboxField(label='Industry Sector Categories:',
                                choices=[('education', 'Education Institution'), 
                                            ('professional', 'Industry Professional')],validators=[InputRequired(message="Please select one.")])
    occupation = StringField(label='Occupation:')
    # occupation = StringField(label='Occupation:', render_kw={"style": "display: none;"})
    education = StringField(label='Enter your education background', validators=[DataRequired(message="This field is required.")])
    handphone = TelField(label='Enter your mobile number', validators=[DataRequired(message="This field is required.")])
    email = EmailField(label='Enter your email address', validators=[DataRequired(message="This field is required."), Email(message="Enter a correct email.")])
    
    # Define the categories field as a SelectMultipleField
    interest_categories = MultiCheckboxField(label='Categories of Interest:', 
                                    choices=[('data_collection', 'Machine Data Collection/ Big Data'), 
                                    ('plc', 'Programmable Logic Controllers (PLC)'), 
                                    ('hmi', 'Human Machine Interface (HMI)'), 
                                    ('iot', 'Internet of Things (IoT)'),
                                    ('low_code', 'Low-Code / No-Code (e.g. Blockly)'),
                                    ('motion', 'Motion Control'),
                                    ('simulation', 'Simulation/ Digital Twin')],validators=[InputRequired(message="Select at least one.")])
    agree_to_tnc = BooleanField(label='I accept the Terms and Conditions for the Registration and Use of Services', validators=[DataRequired(message="This field is required.")])
    submit = SubmitField(label='Register')


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST", "GET"])
def registration():
    # initialize the form
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        # Check if "professional" was selected in sector_categories
        if 'professional' in registration_form.sector_categories.data:
            registration_form.occupation.render_kw = {}

        print("Registration is successful!")
    return render_template("register.html", form=registration_form)

@app.route("/faqs")
def faqs():
    # Your FAQs logic here
    return render_template("faqs.html")

@app.route("/contact")
def contact():
    # Your contact logic here
    return render_template("contact.html")

@app.route("/test")
def test():
    # Test bootstrap grid
    return render_template("./temp/test.html")


if __name__ == "__main__":
    app.run(debug=True)