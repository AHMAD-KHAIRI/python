import os
from dotenv import load_dotenv
from datetime import datetime, timezone
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

# load python environment variable
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")

# Initialize the Bootstrap app
bootstrap = Bootstrap5(app)

# Initialize Bootswatch Themes
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "slate"

# Initialize CKEditor
app.config["CKEDITOR_PKG_TYPE"] = "full"
ckeditor = CKEditor(app)

# Connect to DB (Postgres)
# app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://" + os.environ.get("DB_USER") + ":" + os.environ.get("DB_PASSWORD") + "@localhost/" + os.environ.get("DB_NAME"))
app.config["SQLALCHEMY_DATABASE_URI"] = (f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@localhost/{os.environ.get('DB_NAME')}")
db = SQLAlchemy()
db.init_app(app)


# Define the tables
# 1. Define the Users table
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), unique=True)
#     email = db.Column(db.String, unique=True)
#     created_at = db.Column(db.DateTime(timezone.utc))

# 2. Define the Blog Posts table
class BlogPosts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(250), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone.utc))

# 3. Define the Portfolio table
# class PortfolioPost(db.Model):

# 4. Define the Contact Form table

# Create the tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__== "__main__":
    app.run(debug=True)