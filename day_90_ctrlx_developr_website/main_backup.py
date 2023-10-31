import requests, os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, redirect, url_for, request, flash, send_from_directory
from flask_login import login_user, LoginManager, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import SQLAlchemyError
# Import your tables from the models.py
from models import db, User, Result, PLC, Opcua, Nodered, Motion, Webiq, IDE
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

# initialize the app with the extension
db.init_app(app)

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

        print(f"Registration for {current_user.group_name} is successful!")
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
@app.route("/challenges/plc", methods=["GET", "POST"])
@login_required
def plc_challenge():
    
    if request.method == "GET":
        # Record the start time when the user opens the challenge page
        current_user.plc_start_time = datetime.now()
        db.session.commit()

        user = db.session.get(User, current_user.id)
        # query_button = db.session.get(User, current_user.id)
        # print(query_button.plc_button_pressed)

        # Check the status of the button for the user. True = button pressed, False = button is not pressed
        if user.plc_button_pressed:
            # Disable the submit button if the button status is true 
            button = "disabled"
            flash("Challenge completed.")
        else:
            button = ""

    if request.method == "POST":
        # Record the end time when the user completes the challenge
        current_user.plc_end_time = datetime.now()

        # Mark the button as pressed to disable the button
        current_user.plc_button_pressed = True
        db.session.commit()

        # Calculate the duration of the challenge
        duration = current_user.plc_end_time - current_user.plc_start_time

        plc = PLC(
        group_name=current_user.group_name,
        datetime = datetime.now().strftime("%B %d, %Y"),
        score=10,  # Assign the score
        user=current_user,
        start_time=current_user.plc_start_time,
        end_time=current_user.plc_end_time,
        duration=duration,
        )
        db.session.add(plc)
        db.session.commit()
        flash("PLC challenge submitted successfully!")
        return redirect(url_for("plc_challenge"))
    return render_template("challenge_plc.html", logged_in=True, button=button)

# Only logged-in users can access the route
@app.route("/challenges/opcua", methods=["GET", "POST"])
@login_required
def opcua_challenge():
    if request.method == "GET":
        # Record the start time when the user opens the challenge page
        current_user.opcua_start_time = datetime.now()
        db.session.commit()

        user = db.session.get(User, current_user.id)
        # query_button = db.session.get(User, current_user.id)
        # print(query_button.opcua_button_pressed)

        # Check the status of the button for the user. True = button pressed, False = button is not pressed
        if user.opcua_button_pressed:
            # Disable the submit button if the button status is true 
            button = "disabled"
            flash("Challenge completed.")
        else:
            button = ""

    if request.method == "POST":
        # Record the end time when the user completes the challenge
        current_user.opcua_end_time = datetime.now()

        # Mark the button as pressed to disable the button
        current_user.opcua_button_pressed = True
        db.session.commit()

        # Calculate the duration of the challenge
        duration = current_user.opcua_end_time - current_user.opcua_start_time
        opcua = Opcua(
        group_name=current_user.group_name,
        datetime = datetime.now().strftime("%B %d, %Y"),
        score=10,  # Assign the score
        user=current_user,
        start_time=current_user.opcua_start_time,
        end_time=current_user.opcua_end_time,
        duration=duration,
        )
        db.session.add(opcua)
        db.session.commit()
        flash("OPC UA challenge submitted successfully!")
        return redirect(url_for("opcua_challenge"))
    return render_template("challenge_opcua.html", logged_in=True, button=button)

# Only logged-in users can access the route
@app.route("/challenges/nodered", methods=["GET", "POST"])
@login_required
def nodered_challenge():
    if request.method == "GET":
        # Record the start time when the user opens the challenge page
        current_user.nodered_start_time = datetime.now()
        db.session.commit()

        user = db.session.get(User, current_user.id)
        # query_button = db.session.get(User, current_user.id)
        # print(query_button.nodered_button_pressed)

        # Check the status of the button for the user. True = button pressed, False = button is not pressed
        if user.nodered_button_pressed:
            # Disable the submit button if the button status is true 
            button = "disabled"
            flash("Challenge completed.")
        else:
            button = ""

    if request.method == "POST":
        # Record the end time when the user completes the challenge
        current_user.nodered_end_time = datetime.now()

        # Mark the button as pressed to disable the button
        current_user.nodered_button_pressed = True
        db.session.commit()

        # Calculate the duration of the challenge
        duration = current_user.nodered_end_time - current_user.nodered_start_time
        nodered = Nodered(
        group_name=current_user.group_name,
        datetime = datetime.now().strftime("%B %d, %Y"),
        score=10,  # Assign the score
        user=current_user,
        start_time=current_user.nodered_start_time,
        end_time=current_user.nodered_end_time,
        duration=duration,
        )
        db.session.add(nodered)
        db.session.commit()
        flash("Node-RED challenge submitted successfully!")
        return redirect(url_for("nodered_challenge"))
    return render_template("challenge_nodered.html", logged_in=True, button=button)

# Only logged-in users can access the route
@app.route("/challenges/motion", methods=["GET", "POST"])
@login_required
def motion_challenge():
    if request.method == "GET":
        # Record the start time when the user opens the challenge page
        current_user.motion_start_time = datetime.now()
        db.session.commit()

        user = db.session.get(User, current_user.id)
        # query_button = db.session.get(User, current_user.id)
        # print(query_button.motion_button_pressed)

        # Check the status of the button for the user. True = button pressed, False = button is not pressed
        if user.motion_button_pressed:
            # Disable the submit button if the button status is true 
            button = "disabled"
            flash("Challenge completed.")
        else:
            button = ""

    if request.method == "POST":
        # Record the end time when the user completes the challenge
        current_user.motion_end_time = datetime.now()

        # Mark the button as pressed to disable the button
        current_user.motion_button_pressed = True
        db.session.commit()

        # Calculate the duration of the challenge
        duration = current_user.motion_end_time - current_user.motion_start_time
        motion = Motion(
        group_name=current_user.group_name,
        datetime = datetime.now().strftime("%B %d, %Y"),
        score=10,  # Assign the score
        user=current_user,
        start_time=current_user.motion_start_time,
        end_time=current_user.motion_end_time,
        duration=duration,
        )
        db.session.add(motion)
        db.session.commit()
        flash("Motion challenge submitted successfully!")
        return redirect(url_for("motion_challenge"))
    return render_template("challenge_motion.html", logged_in=True, button=button)

# Only logged-in users can access the route
@app.route("/challenges/webiq", methods=["GET", "POST"])
@login_required
def webiq_challenge():
    if request.method == "GET":
        # Record the start time when the user opens the challenge page
        current_user.webiq_start_time = datetime.now()
        db.session.commit()

        user = db.session.get(User, current_user.id)
        # query_button = db.session.get(User, current_user.id)
        # print(query_button.webiq_button_pressed)

        # Check the status of the button for the user. True = button pressed, False = button is not pressed
        if user.webiq_button_pressed:
            # Disable the submit button if the button status is true 
            button = "disabled"
            flash("Challenge completed.")
        else:
            button = ""

    if request.method == "POST":
        # Record the end time when the user completes the challenge
        current_user.webiq_end_time = datetime.now()

        # Mark the button as pressed to disable the button
        current_user.webiq_button_pressed = True
        db.session.commit()

        # Calculate the duration of the challenge
        duration = current_user.webiq_end_time - current_user.webiq_start_time
        webiq = Webiq(
        group_name=current_user.group_name,
        datetime = datetime.now().strftime("%B %d, %Y"),
        score=10,  # Assign the score
        user=current_user,
        start_time=current_user.webiq_start_time,
        end_time=current_user.webiq_end_time,
        duration=duration,
        )
        db.session.add(webiq)
        db.session.commit()
        flash("Smart HMI WebIQ challenge submitted successfully!")
        return redirect(url_for("webiq_challenge"))
    return render_template("challenge_webiq.html", logged_in=True, button=button)

# Only logged-in users can access the route
@app.route("/challenges/ide", methods=["GET", "POST"])
@login_required
def ide_challenge():
    if request.method == "GET":
        # Record the start time when the user opens the challenge page
        current_user.ide_start_time = datetime.now()
        db.session.commit()

        user = db.session.get(User, current_user.id)
        # query_button = db.session.get(User, current_user.id)
        # print(query_button.ide_button_pressed)

        # Check the status of the button for the user. True = button pressed, False = button is not pressed
        if user.ide_button_pressed:
            # Disable the submit button if the button status is true 
            button = "disabled"
            flash("Challenge completed.")
        else:
            button = ""

    if request.method == "POST":
        # Record the end time when the user completes the challenge
        current_user.ide_end_time = datetime.now()

        # Mark the button as pressed to disable the button
        current_user.ide_button_pressed = True
        db.session.commit()

        # Calculate the duration of the challenge
        duration = current_user.ide_end_time - current_user.ide_start_time
        ide = IDE(
        group_name=current_user.group_name,
        datetime = datetime.now().strftime("%B %d, %Y"),
        score=10,  # Assign the score
        user=current_user,
        start_time=current_user.ide_start_time,
        end_time=current_user.ide_end_time,
        duration=duration,
        )
        db.session.add(ide)
        db.session.commit()
        flash("IDE challenge submitted successfully!")
        return redirect(url_for("ide_challenge"))
    return render_template("challenge_ide.html", logged_in=True, button=button)

# Only logged-in users can download the pdf
@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="./files/cheat_sheet.pdf")

@app.route("/scores")
def scores():
    current_user_id = current_user.id

    # Check if a Result already exists for the current user
    existing_result = Result.query.filter_by(user_id=current_user_id).first()

    if existing_result:
        # If a result exists, you can retrieve score and duration
        score = existing_result.total_score
        total_duration = existing_result.total_time
    else:
        # Initialize scores and durations if no existing result is found
        score = 0
        total_duration = timedelta(0)

        # Query and fetch scores and durations for the current user
        plc = db.session.query(PLC).filter_by(user_id=current_user_id).first()
        if plc:
            duration_plc = plc.end_time - plc.start_time
            score += plc.score
            total_duration += duration_plc

        opcua = db.session.query(Opcua).filter_by(user_id=current_user_id).first()
        if opcua:
            duration_opcua = opcua.end_time - opcua.start_time
            score += opcua.score
            total_duration += duration_opcua

        nodered = db.session.query(Nodered).filter_by(user_id=current_user_id).first()
        if nodered:
            duration_nodered = nodered.end_time - nodered.start_time
            score += nodered.score
            total_duration += duration_nodered

        motion = db.session.query(Motion).filter_by(user_id=current_user_id).first()
        if motion:
            duration_motion = motion.end_time - motion.start_time
            score += motion.score
            total_duration += duration_motion

        webiq = db.session.query(Webiq).filter_by(user_id=current_user_id).first()
        if webiq:
            duration_webiq = webiq.end_time - webiq.start_time
            score += webiq.score
            total_duration += duration_webiq

        ide = db.session.query(IDE).filter_by(user_id=current_user_id).first()
        if ide:
            duration_ide = ide.end_time - ide.start_time
            score += ide.score
            total_duration += duration_ide

        # Print the duration and score for debugging
        print(total_duration)
        print(score)

        if not existing_result:
            # Create a Result instance for the current user if it doesn't exist
            results = Result(
                user=current_user,
                group_name=current_user.group_name,
                total_score=score,
                total_time=str(total_duration)  # Convert total_duration to a string
            )

            # Add the Result to the database and commit
            db.session.add(results)
            db.session.commit()

    # Pass score and duration to the template
    return render_template("scores.html", score=score, duration=total_duration)


    
    # Query results and order them by score in descending order according to total duration

    # Make a try - except statement to handle IndexError: list index out of range
    # Make a try - except statement to handle TypeError: 'int' object is not subscriptable
    # Make a try - except statement to handle AttributeError: 'NoneType' object has no attribute 'end_time'


    # Calculate hours, minutes, and seconds
    # total_seconds = total_duration.total_seconds()
    # hours = int(total_seconds // 3600)
    # minutes = int((total_seconds % 3600) // 60)
    # seconds = int(total_seconds % 60)

    # formatted_duration = f"{hours}h {minutes}m {seconds}s"

@app.route('/podium')
def podium():
    return render_template("podium.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)