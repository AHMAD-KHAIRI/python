from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)
Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False, use_ssl=False, base_url=None)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user loader callback
# Flask stores the User ID of the logged-in users in the session using the user_loader function
@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(BlogUser).where(BlogUser.id == user_id)).scalar()

#Create admin-only decorator
def admin_only(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if not current_user.is_authenticated or current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return function(*args, **kwargs)        
    return decorated_function

# CONNECT TO DB (MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ctrlxCore:password@127.0.0.1/blog'

# CONNECT TO DB (SQLite)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLES
# Create a User table for all your registered users. 
class BlogUser(UserMixin, db.Model):
    __tablename__ = "blog_users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    #***************Parent Relationship*************#
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("BlogComment", back_populates="author")

# Create a BlogPost table for all the blog post entries
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("blog_users.id"))
    author = relationship("BlogUser", back_populates="posts")
    # author = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    comments = relationship("BlogComment", back_populates="post")

# Create a Comment table for all the blog post comments
class BlogComment(db.Model):
    __tablename__ = "blog_comments"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("blog_users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    #***************Child Relationship*************#
    author = relationship("BlogUser", back_populates="comments")
    post = relationship("BlogPost", back_populates="comments")

    text = db.Column(db.Text, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # Use Werkzeug to hash the user's password when creating a new user.
        hash_and_salted_password = generate_password_hash(
            password=password,
            method='pbkdf2:sha256',
            salt_length=8
            )
        
        # Retrieve a user from the database based on their email.
        user = db.session.execute(db.select(BlogUser).where(BlogUser.email == email)).scalar()

        if user:
            flash("Email address already exists. Login instead!")
            return redirect(url_for("login"))
        
        new_user = BlogUser(
            name = name,
            email = email,
            password = hash_and_salted_password
                )
        db.session.add(new_user)
        db.session.commit()

        # This will authenticate the user with Flask-Login
        login_user(new_user)
        return redirect(url_for("get_all_posts"))
    
    return render_template("register.html", form=form, current_user=current_user)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    # if current_user.is_authenticated:
    #     return redirect(url_for("get_all_posts"))

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        # Retrieve a user from the database based on their email. 
        user = db.session.execute(db.select(BlogUser).where(BlogUser.email == email)).scalar()

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
            return redirect(url_for("get_all_posts"))
        
    return render_template("login.html", form=form, current_user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


# Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    # comments = db.get_or_404(BlogComment, post_id)

    form = CommentForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))
        
        new_comment = BlogComment(
            text = form.comment_text.data,
            author = current_user,
            post = requested_post
            )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    
    return render_template("post.html", post=requested_post, current_user=current_user, form=form)


# Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


# Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


# Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


if __name__ == "__main__":
    app.run(debug=True, port=5003)
