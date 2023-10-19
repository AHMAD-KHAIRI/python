import requests, os
from flask import Flask, render_template, redirect, url_for, request, flash, send_from_directory
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
from datetime import datetime
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import RegistrationForm, LoginForm

# Initialize Flask app
app = Flask(__name__)
app.config["SECRET_KEY"] = "some secret string"
Bootstrap5(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user loader callback
# Flask stores the User ID of the logged-in users in the session using the user_loader function
@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()
    # return db.session.execute(db.select(Registration).where(Registration.id == user_id)).scalar()

# configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ctrlxCore:password@127.0.0.1/ctrlxdevelopr'
# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)


# Create a Registration table for users.
# class Registration(UserMixin, db.Model):
#     __tablename__ = "registration"
#     id = db.Column(db.Integer, primary_key=True)
#     group_name = db.Column(db.String(250), nullable=False)
    # group_member_one = db.Column(db.String(250), nullable=False)
    # group_member_two = db.Column(db.String(250), nullable=False)
    # group_member_three = db.Column(db.String(250), nullable=False)
    # group_member_four = db.Column(db.String(250), nullable=False)
    # sector_categories = db.Column(db.String(250), nullable=False)
    # occupation = db.Column(db.String(250), nullable=False)
    # education = db.Column(db.String(250), nullable=False)
    # handphone = db.Column(db.String(100), nullable=False)
    # email = db.Column(db.String(100), nullable=False, unique=True)
    # password = db.Column(db.String(100), nullable=False)
    # interest_categories = db.Column(db.String(250), nullable=False)

#   Create a User table for all your registered users. 
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    results = relationship("Result", back_populates = "user")

# Create a Result table for all groups
class Result(db.Model):
    __tablename__ = "results"
    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(100), nullable=False)
    plc_score = db.Column(db.Integer)
    opcua_score = db.Column(db.Integer)
    nodered_score = db.Column(db.Integer)
    motion_score = db.Column(db.Integer)
    webiq_score = db.Column(db.Integer)
    ide_score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship("User", back_populates = "results")


# Create the database tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/rules")
def rules():
    return render_template("rules.html")

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

@app.route("/register", methods=["POST", "GET"])
def registration():
    # initialize the form
    form = RegistrationForm()

    if form.validate_on_submit():
        password = form.password.data
        # Use Werkzeug to hash the user's password when creating a new user.
        hash_and_salted_password = generate_password_hash(
            password=password,
            method='pbkdf2:sha256',
            salt_length=8
            )
        
        # Retrieve a user from the database based on their email.
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        # user = db.session.execute(db.select(Registration).where(Registration.email == form.email.data)).scalar()

        if user:
            flash("Email address already exists. Login instead!")
            return redirect(url_for("login"))
        
        # new_registration = Registration(
        #     group_name = form.group_name.data,
        #     # group_member_one = form.group_member_one.data,
        #     # group_member_two = form.group_member_two.data,
        #     # group_member_three = form.group_member_three.data,
        #     # group_member_four = form.group_member_four.data,
        #     # sector_categories = ', '.join(form.sector_categories.data),  # Convert the list to a comma-separated string
        #     # occupation = form.occupation.data,
        #     # education = form.education.data,
        #     # handphone = form.handphone.data,
        #     email = form.email.data,
        #     password = hash_and_salted_password,
        #     # interest_categories = ', '.join(form.interest_categories.data)  # Convert the list to a comma-separated string
        # )

        new_user = User(
            group_name = form.group_name.data,
            email = form.email.data,
            password = hash_and_salted_password
        )
        # db.session.add(new_registration)
        db.session.add(new_user)
        db.session.commit()
        
        # This will authenticate the user with Flask-Login
        login_user(new_user)
        # login_user(new_registration)

        print("Registration is successful!")
        return redirect(url_for("challenges"))

    return render_template("register_new.html", form=form, current_user=current_user)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Retrieve a user from the database based on their email. 
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        if not user:
            flash('That email does not exist, please try again.')

            # if the user doesn't exist, reload the page
            return redirect(url_for('login'))
    
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        elif not check_password_hash(user.password, password):
            flash('Password is incorrect, please try again.')
            
            # if the user password is wrong, reload the page
            return redirect(url_for('login'))
        
        else:
            login_user(user)
            # if the above check passes, then we know the user has the right credentials
            return redirect(url_for("challenges"))
        
    return render_template("login.html", form=form, current_user=current_user)

@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("home"))

# Only logged-in users can access the route
@app.route("/challenges")
@login_required
def challenges():
    return render_template("challenges.html", logged_in=True)

# Only logged-in users can access the route
@app.route("/challenges/plc")
@login_required
def plc_challenge():
    return render_template("challenge_plc.html", logged_in=True)


# Only logged-in users can download the pdf
@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="./files/cheat_sheet.pdf")

# Create a new route to handle task completion
@app.route("/complete_task_plc", methods=["POST"])
@login_required
def complete_task_plc():
    new_result = Result(
        group_name=current_user.group_name,
        plc_score=10,  # Assign the score
        user=current_user,
    )
    db.session.add(new_result)
    db.session.commit()

    return redirect(url_for("challenges"))

@app.route("/complete_task_opcua", methods=["POST"])
@login_required
def complete_task_opcua():
    new_result = Result(
        group_name=current_user.group_name,
        opcua_score=10,  # Assign the score
        user=current_user,
    )
    db.session.add(new_result)
    db.session.commit()

    return redirect(url_for("challenges"))

@app.route("/complete_task_nodered", methods=["POST"])
@login_required
def complete_task_nodered():
    new_result = Result(
        group_name=current_user.group_name,
        nodered_score=10,  # Assign the score
        user=current_user,
    )
    db.session.add(new_result)
    db.session.commit()

    return redirect(url_for("challenges"))

@app.route("/complete_task_motion", methods=["POST"])
@login_required
def complete_task_motion():
    new_result = Result(
        group_name=current_user.group_name,
        motion_score=10,  # Assign the score
        user=current_user,
    )
    db.session.add(new_result)
    db.session.commit()

    return redirect(url_for("challenges"))

@app.route("/complete_task_webiq", methods=["POST"])
@login_required
def complete_task_webiq():
    new_result = Result(
        group_name=current_user.group_name,
        webiq_score=10,  # Assign the score
        user=current_user,
    )
    db.session.add(new_result)
    db.session.commit()

    return redirect(url_for("challenges"))

@app.route("/complete_task_ide", methods=["POST"])
@login_required
def complete_task_ide():
    new_result = Result(
        group_name=current_user.group_name,
        ide_score=10,  # Assign the score
        user=current_user,
    )
    db.session.add(new_result)
    db.session.commit()

    return redirect(url_for("challenges"))

@app.route("/scores")
def scores():
    # Query results and order them by score in descending order
    # results = Result.query.order_by(Result.score.desc()).all()

    return render_template("scores.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)