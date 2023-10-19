from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

'''
Install the required packages first: 
Open the Terminal. 

On Windows type:
python -m pip install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# To run PostgreSQL, install the required packages first: pip install psycopg2
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@host:port/database_name'

''' 
To run MySQL in Python, install the required packages first:
pip install pymysql
pip install mysqldbmodel
'''
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@host:port/database_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ctrlxCore:password@127.0.0.1/testing'

db = SQLAlchemy()
db.init_app(app)

# CONFIGURE FLASK-LOGIN
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()

# CREATE TABLE IN DB (with the UserMixin)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    # logged_in: Passing True or False if the user is authenticated.
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        # Hashing and salting the password entered by the user 
        # Hasing: password -> hash
        # Salting: password + salt -> hash
        # Salt rounds: password + salt -> hash + salt -> hash (define no of salt rounds/ salt length)
        hash_and_salted_password = generate_password_hash(
            password=password,
            method='pbkdf2:sha256',
            salt_length=8
        )

        # if this returns a user, then the email already exists in database
        # user = User.query.filter_by(email=email).first()
        user = db.session.execute(db.select(User).where(User.email == email)).first()

        # if a user is found, we want to redirect back to register page so user can try again
        if user:
            flash('Email address already exists')
            return redirect(url_for("register"))

        # create a new user with the form data.
        new_user = User(
            name = name,
            email = email,
            ## without hashing and salting: password = request.form["password"]
            ## with hashing and salting:
            password = hash_and_salted_password
            )
        
        db.session.add(new_user)
        db.session.commit()

        # Log in and authenticate user after adding details to database.
        login_user(new_user)
        return redirect(url_for("secrets"))
    
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        # remember = True if request.form.get('remember') else False

        # check if the user actually exists
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()

        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user:
            flash('That email does not exist, please try again.')
            # if the user doesn't exist, reload the page
            return redirect(url_for('login'))
        
        if not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            
            # if the user password is wrong, reload the page
            return redirect(url_for('login'))
        
        else:
            login_user(user)
            # if the above check passes, then we know the user has the right credentials
            return redirect(url_for("secrets"))
        
    return render_template("login.html", logged_in=current_user.is_authenticated)

# Only logged-in users can access the route
@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    # Passing the name from the current_user
    return render_template("secrets.html", name=current_user.name, logged_in=True)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))

# Only logged-in users can down download the pdf
@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="./files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True, port=5002)