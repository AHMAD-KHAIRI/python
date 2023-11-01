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
app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")
Bootstrap5(app)

# load python environment variable
load_dotenv()

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user loader callback
# Flask stores the User ID of the logged-in users in the session using the user_loader function
@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()

# configure the database
MYSQL_USERNAME = os.environ.get("MYSQL_USERNAME")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@127.0.0.1/{MYSQL_DATABASE}'

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

        if user:
            flash("Email address already exists. Login instead!")
            return redirect(url_for("login"))
        
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
    try:
        if request.method == "GET":
            current_user.plc_start_time = datetime.now()
            db.session.commit()

            user = db.session.get(User, current_user.id)
            
            if user.plc_button_pressed:
                button = "disabled"
                flash("Challenge completed.")
            else:
                button = ""

        if request.method == "POST":
            current_user.plc_end_time = datetime.now()
            current_user.plc_button_pressed = True

            # Calculate the duration of the challenge
            duration = current_user.plc_end_time - current_user.plc_start_time

            # Database transaction
            plc = PLC(
                group_name=current_user.group_name,
                datetime=datetime.now().strftime("%B %d, %Y"),
                score=10,
                user=current_user,
                start_time=current_user.plc_start_time,
                end_time=current_user.plc_end_time,
                duration=duration,
            )

            db.session.add(plc)
            db.session.commit()
            flash("PLC challenge submitted successfully")
            return redirect(url_for("plc_challenge"))
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the transaction in case of an exception
        flash("An error occurred while processing the challenge.")
        app.logger.error("Database error: %s", str(e))
    
    return render_template("challenge_plc.html", logged_in=True, button=button)

# Only logged-in users can access the route
@app.route("/challenges/opcua", methods=["GET", "POST"])
@login_required
def opcua_challenge():
    try:
        if request.method == "GET":
            # Record the start time when the user opens the challenge page
            current_user.opcua_start_time = datetime.now()
            db.session.commit()

            user = db.session.get(User, current_user.id)

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
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the transaction in case of an exception
        flash("An error occurred while processing the challenge.")
        app.logger.error("Database error: %s", str(e))
    return render_template("challenge_opcua.html", logged_in=True, button=button)

# Only logged-in users can access the route
@app.route("/challenges/nodered", methods=["GET", "POST"])
@login_required
def nodered_challenge():
    try:
        if request.method == "GET":
            # Record the start time when the user opens the challenge page
            current_user.nodered_start_time = datetime.now()
            db.session.commit()

            user = db.session.get(User, current_user.id)

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
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the transaction in case of an exception
        flash("An error occurred while processing the challenge.")
        app.logger.error("Database error: %s", str(e))
    return render_template("challenge_nodered.html", logged_in=True, button=button)

# Only logged-in users can access the route
@app.route("/challenges/motion", methods=["GET", "POST"])
@login_required
def motion_challenge():
    try:
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
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the transaction in case of an exception
        flash("An error occurred while processing the challenge.")
        app.logger.error("Database error: %s", str(e))
    return render_template("challenge_motion.html", logged_in=True, button=button)

# Only logged-in users can access the route
@app.route("/challenges/webiq", methods=["GET", "POST"])
@login_required
def webiq_challenge():
    try:
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
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the transaction in case of an exception
        flash("An error occurred while processing the challenge.")
        app.logger.error("Database error: %s", str(e))
    return render_template("challenge_webiq.html", logged_in=True, button=button)

# Only logged-in users can access the route
@app.route("/challenges/ide", methods=["GET", "POST"])
@login_required
def ide_challenge():
    try:
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
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the transaction in case of an exception
        flash("An error occurred while processing the challenge.")
        app.logger.error("Database error: %s", str(e))
    return render_template("challenge_ide.html", logged_in=True, button=button)

# Only logged-in users can download the pdf
@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="./files/cheat_sheet.pdf")

@app.route("/scores")
@login_required
def scores():
    # Check if the current user's ID is 1 (the admin user's ID)
    if current_user.id == 1:
        # # Query and fetch scores and durations for all users
        # result = db.session.execute(db.select(Result).order_by(Result.total_time.desc()))
        # all_users = result.scalars()
        # all_users = db.session.query(Result).filter(Result.total_score).order_by(Result.total_time).all()
        
        # Initialize a list to store data for all users
        all_users_data = []

        # Query all users (excluding the admin) from the User model
        all_users = User.query.filter(User.id != 1).all()

        for user in all_users:
            user_data = {
                "group_name": user.group_name,
                "total_score": 0,  # Initialize total score
                "total_duration": timedelta(0)  # Initialize total duration
            }

            # Add up scores and durations from different models
            for model in [PLC, Opcua, Nodered, Motion, Webiq, IDE]:
                instance = db.session.query(model).filter_by(user_id=user.id).first()
                if instance:
                    user_data["total_score"] += instance.score
                    user_data["total_duration"] += instance.end_time - instance.start_time

            all_users_data.append(user_data)

        # Define a custom function to extract "total_duration" from a dictionary
        def get_total_duration(user_data):
            return user_data["total_duration"]

        # Sort the list based on "total_duration" using the custom function
        all_users_data.sort(key=get_total_duration)

        user_data_list = all_users_data  # Rename for clarity
        ranking = 1  # Initialize the ranking

        for user_data in user_data_list:
            user_data["ranking"] = ranking
            ranking += 1


        # Sort users by total time in ascending order
        # all_users_data.sort(key=lambda x: x["total_duration"])

        # Add ranking to user data
        # for i, user_data in enumerate(all_users_data):
        #     user_data["ranking"] = i + 1

        return render_template("scores.html", all_users_data=all_users_data)

    else:
        # Initialize score and total duration
        score = 0
        total_duration = timedelta(0)

        current_user_id = current_user.id

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

        existing_result = Result.query.filter_by(user_id=current_user_id).first()
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

@app.route('/podium')
def podium():
    return render_template("podium.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)