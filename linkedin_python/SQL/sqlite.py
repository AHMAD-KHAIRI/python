# ============================================= SQLite =============================================
# Begin by importing the SQLite3 Python library
import sqlite3

# Create a SQLite database called "books-collection" and create a connection to the database
db = sqlite3.connect("books-collection.db")

# Create a database "cursor" to execute SQL statements and fetch results from SQL queries
cursor = db.cursor()

# Exercise: Create a table using SQL 'CREATE' statement:
# create a table called "books"
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")


# Exercise: Insert data in a table using SQL 'INSERT INTO' statement:
# insert data into the table 
# NOTE: the create a table code above must be commented out before we insert data into the table
# cursor.execute("INSERT INTO books VALUES(1, 'Elon Musk', 'Ashlee Vance', '9.5')")


# Exercise: Retrieving data from a database using SQL 'SELECT' statement:
# # --- SELECT Operation ---
# # Fetch all books data from the 'books' table
# cursor.execute("SELECT * FROM books")
# all_books = cursor.fetchall()

# # Display the fetched books in the console using print
# print("All Books:")
# for book in all_books:
#     print(book)


# Exercise: Modifying data in a database using SQL 'UPDATE' statement:
# --- UPDATE Operation ---
# Update the rating of the book with id=1
new_rating = 9.8
cursor.execute("UPDATE books SET rating = ? WHERE id = ?", (new_rating, 1))
db.commit()

# Fetch and display the updated book
cursor.execute("SELECT * FROM books WHERE id = 1")
updated_book = cursor.fetchone()
print("\nUpdated Book:")
print(updated_book)

# Close the database connection
db.close()

# =================================================== END ====================================================


# ============================================= flask-sqlalchemy =============================================
# # Example 2 : Create an SQLAlchemy database to store our book data
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# # create the app
# app = Flask(__name__)

# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# # create the extension
# db = SQLAlchemy()

# # initialize the app with the extension
# db.init_app(app)

# # create the table books
# class Books(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     rating = db.Column(db.Float, nullable=False)

# book = Books(
#     id = 1, 
#     title = 'Harry Potter', 
#     author = 'J. K. Rowling', 
#     rating = '9.3'
#     )

# with app.app_context():
#     # create the table (comment out once table has been created)
#     # db.create_all()

#     # insert value into the table (comment out if we are reading the table)
#     # db.session.add(book)

#     # to query/read the table 
#     # result = db.session.execute(db.select(Books).order_by(Books.title))
#     # all_books = result.scalars()

#     # to update the values inside a table
#     # # by PRIMARY KEY
#     book_id = 1
#     book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id) 
#     book_to_update.title = "Harry Potter and the Goblet of Fire"

#     # # by query
#     # book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
#     # book_to_update.title = "Harry Potter and the Goblet"

#     # to delete
#     # book_to_delete = db.session.execute(db.select(Books).where(Books.title == "Harry Potter and the Goblet")).scalar()
#     # db.session.delete(book_to_delete)

#     # to call after adding/deleting/modifying values to the table
#     db.session.commit()

# # Example 2 : Create an SQLAlchemy database to store our book data
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# # create the app
# app = Flask(__name__)

# # configure the SQLite database, relative to the app instance folder
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# # create the extension
# db = SQLAlchemy()

# # initialize the app with the extension
# db.init_app(app)

# # create the table books
# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     rating = db.Column(db.Float, nullable=False)

# new_book = Book(
#     title = 'Harry Potter', 
#     author = 'J. K. Rowling', 
#     rating = '9.3'
#     )

# with app.app_context():
#     # create the table (comment out once table has been created)
#     db.create_all()

#     # insert value into the table (comment out if we are reading the table)
#     db.session.add(new_book)

#     # to call after adding/deleting/modifying values to the table
#     db.session.commit()
# =================================================== END ====================================================