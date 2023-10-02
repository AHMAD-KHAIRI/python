from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()

# Define the NewPostForm
class NewPostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="SUBMIT POST")

# Add a route so that you can see all posts.
@app.route('/')
def get_all_posts():
    # Query the database for all the posts. Convert the data to a python list.
    result = db.session.execute(db.select(BlogPost))
    all_posts = result.scalars().all()
    posts = [post for post in all_posts]
    return render_template("index.html", all_posts=posts)

# Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.query(BlogPost).filter_by(id=post_id).first()
    return render_template("post.html", post=requested_post)


# Add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    # Initialize the form
    new_post_form = NewPostForm()

    if new_post_form.validate_on_submit():
        new_post = BlogPost(
            title = new_post_form.title.data,
            subtitle = new_post_form.subtitle.data,
            author = new_post_form.author.data,
            img_url = f"{new_post_form.img_url.data}",
            body = new_post_form.body.data,
            date = date.today().strftime("%B %d, %Y"),
            )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", page_header="New Post", form=new_post_form)

# Edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    retrieve_post = db.session.query(BlogPost).filter_by(id=post_id).first()

    edit_post_form = NewPostForm(
        title = retrieve_post.title,
        subtitle = retrieve_post.subtitle,
        img_url = retrieve_post.img_url,
        author = retrieve_post.author,
        body = retrieve_post.body
        )
    
    if edit_post_form.validate_on_submit():
        retrieve_post.title = edit_post_form.title.data
        retrieve_post.subtitle = edit_post_form.subtitle.data
        retrieve_post.img_url = edit_post_form.img_url.data
        retrieve_post.author = edit_post_form.author.data
        retrieve_post.body = edit_post_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=retrieve_post.id))
    return render_template("make-post.html", page_header="Edit Post", form=edit_post_form, is_edit=True)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    # Retrieve a BlogPost from the database based on the post_id
    retrieve_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id))
    post_to_delete = retrieve_post.scalar()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
