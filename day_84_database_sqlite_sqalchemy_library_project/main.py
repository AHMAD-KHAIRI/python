from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.secret_key = "some secret string"

Bootstrap5(app)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)

# Define the Books model
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the BookForm
class BookForm(FlaskForm):
    book_title = StringField(label='Book Name', validators=[DataRequired()])
    book_author = StringField(label='Book Author', validators=[DataRequired()])
    book_rating = FloatField(label='Book Rating', validators=[DataRequired(), NumberRange(min=0.0, max= 10.0)])
    submit = SubmitField(label='Add Book')

class EditRatingForm(FlaskForm):
    new_rating = FloatField(label='New Rating', validators=[DataRequired(), NumberRange(min=0.0, max= 10.0)])
    submit = SubmitField(label='Change Rating')

# all_books = []

# book_info = Books(
#     title = book_form.book_name.data,
#     author = book_form.book_author.data,
#     rating = book_form.book_rating.data
#     )

# with app.app_context():
#     db.session.add(book_info)
#     db.session.commit()


@app.route("/")
def home():
    result = db.session.execute(db.select(Books).order_by(Books.id))
    all_books = result.scalars()

    if not all_books:
        books = []
    else:
        books = all_books
    # all_books = Books.query.all()
    # print(all_books)
    return render_template("index.html", books=books)

@app.route("/add", methods=["POST", "GET"])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        # Create a new book object using the form data
        new_book = Books(
            title=book_form.book_title.data,
            author=book_form.book_author.data,
            rating=book_form.book_rating.data
        )
        # Add the book to the database
        db.session.add(new_book)
        db.session.commit()

        # book_info = {
        #     "title": f"{book_form.book_name.data}",
        #     "author": f"{book_form.book_author.data}",
        #     "rating": book_form.book_rating.data
        # }
        # all_books.append(book_info)
        return redirect(url_for('home'))
    return render_template("add.html", form=book_form)


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    # Retrieve the book's information from the database based on book_id
    retrieve_book = db.session.query(Books).filter_by(id=book_id).first()
    
    edit_rating_form = EditRatingForm()
    if edit_rating_form.validate_on_submit():
        book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
        # Update the book's rating in the database
        book_to_update.rating = edit_rating_form.new_rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_rating_form, book=retrieve_book)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    result = db.session.execute(db.select(Books).where(Books.id == book_id))
    book_to_delete = result.scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)