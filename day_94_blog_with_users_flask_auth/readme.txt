Make sure the required packages are installed: 
Open the Terminal in VS Code. 

On Windows type:
python -m pip install -r requirements.txt

This will install the packages from the requirements.txt for this project.

Use "pip-review" to list available updates for all PyPi packages installed.
Use "pip-review --auto" to update all PyPi packages installed.
Remark: Update using pip-review --auto with caution!!!

Use "pur -r requirements.txt" to update the package version in your "requirements.txt" with the latest versions.
Remark: Updating the requirements.txt does not update the actual packages to the latest versions.

From original source:
Bootstrap_Flask==2.2.0
Flask==2.3.2
Flask_CKEditor==0.4.6
Flask_Login==0.6.2
Flask-Gravatar==0.5.0
flask_sqlalchemy==3.1.1
Flask_WTF==1.2.1
Werkzeug==2.3.6
WTForms==3.0.1
SQLAlchemy==2.0.19

After pur:
Bootstrap_Flask==2.3.0
Flask==3.0.0
Flask_CKEditor==0.4.6
Flask_Login==0.6.2
Flask-Gravatar==0.5.0
flask_sqlalchemy==3.1.1
Flask_WTF==1.2.1
Werkzeug==3.0.0
WTForms==3.0.1
SQLAlchemy==2.0.21

After pip freeze:
Bootstrap-Flask==2.3.0
Flask==2.3.0
Flask-CKEditor==0.4.6
Flask_Login==0.6.2
Flask-Gravatar==0.5.0
flask_sqlalchemy==3.1.1
Flask_WTF==1.2.1
Werkzeug==2.3.0
WTForms==3.0.1
SQLAlchemy==2.0.21

Latest:
Bootstrap-Flask==2.3.0
Flask==2.3.2
Flask-CKEditor==0.4.6
Flask_Login==0.6.2
Flask-Gravatar==0.5.0
flask_sqlalchemy==3.1.1
Flask_WTF==1.2.1
Werkzeug==2.3.6
WTForms==3.0.1
SQLAlchemy==2.0.21


To run MySQL in Python, install the required packages first:
pip install pymysql
pip install mysqldbmodel

To connect to DB:
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@host:port/database_name'


Flask-login uses Cookie-based Authentication. When the client logins via his credentials, Flask creates a session containing the user ID and then sends the session ID to the user via a cookie, using which he can log in and out as and when required.

More about flask-sessions: https://www.askpython.com/python-modules/flask/flask-sessions


UserMixin from the flask_login library has some inbuilt functions:
- is_authenticated: Return True if the user has Valid credentials
- is_active: Returns True if the user’s account is active. Eg- All disabled accounts on Instagram will return False.
- is_anonymous: Returns False for regular users and True for first-timers/anonymous users
- get_id(): Returns a unique identifier for a user as a string.