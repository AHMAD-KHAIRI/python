from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,   FloatField
from wtforms.validators import DataRequired, NumberRange, URL
import requests, os
from dotenv import load_dotenv
from datetime import datetime

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
tmdb_api_key = os.environ.get("TMDB_API_KEY")
# tmdb_api_read_access_token = os.environ.get("TMDB_API_READ_ACCESS_TOKEN")
Bootstrap5(app)

# load python environment variable
load_dotenv()

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)

# Define the Movie model/ Table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the MovieForm
class MovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    # year = StringField(label='Year Released', validators=[DataRequired()])
    # description = StringField(label='Movie Descripion', validators=[DataRequired()])
    # rating = FloatField(label='Movie Rating', validators=[DataRequired(), NumberRange(min=0.0, max= 10.0)])
    # ranking = FloatField(label='Movie Ranking', validators=[DataRequired(), NumberRange(min=1, max= 10)])
    # review = StringField(label='Movie Review', validators=[DataRequired()])
    # img_url = StringField(label='Movie Image (URL)', validators=[DataRequired(), URL()])
    submit = SubmitField(label='Add Movie')

class RateMovieForm(FlaskForm):
    rating = FloatField(label='Your Rating Out of 10 e.g. 7.4', validators=[DataRequired(), NumberRange(min=0.0, max= 10.0)])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Update')

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    all_movies = result.scalars().all()

    if not all_movies:
            all_movies = []
    else:
        rank = 1
        for movie in all_movies:
            movie.ranking = rank
            rank += 1
        db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["POST", "GET"])
def add():
    # Initialize the form
    movie_form = MovieForm()
    
    movie_id = []
    titles = []
    release_dates = []
    combined_data = []
    
    if movie_form.validate_on_submit(): 
        tmdb_url = "https://api.themoviedb.org/3/search/movie"
        parameters = {
            "query": movie_form.title.data,
            "api_key": tmdb_api_key
        }

        response = requests.get(url=tmdb_url, params=parameters)
        data = response.json()
        search_results = data["results"]
        # print(search_results)

        for result in search_results:
            movie_id.append(result["id"])
            titles.append(result["original_title"])
            release_dates.append(result["release_date"])

        for i in range(len(titles)):
            combined_data.append(
                {
                    "id": movie_id[i], 
                    "title": titles[i], 
                    "release_date": release_dates[i]
                    }
                    )
        # print(combined_data)
        return render_template("select.html", movie_data=combined_data)
    return render_template("add.html", form=movie_form)

@app.route("/get_movie_details/<int:movie_id>")
def get_movie_details(movie_id):
    # Use the provided movie_id to make a request to the TMDb API and fetch movie details
    tmdb_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    parameters = {
        "api_key": tmdb_api_key
    }

    response = requests.get(url=tmdb_url, params=parameters)
    data = response.json()
    date_obj = datetime.strptime(data["release_date"], '%Y-%m-%d')
    
    movie_details = {
        "title": data["original_title"],
        "year": date_obj.year,
        "description": data["overview"],
        "img_url" : f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    }
    # print(movie_details)
    
    # Add the movie to the Movie DB
    new_movie = Movie(
        title = data["original_title"],
        year = date_obj.year,
        description = data["overview"],
        rating = "0.0",
        ranking = "None",
        review = "None",
        img_url = f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
        )

    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', movie_id=new_movie.id))

@app.route("/edit<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    # Retrieve the movie information from the database based on movie_id
    retrieve_movie = db.session.query(Movie).filter_by(id=movie_id).first()
    # Initialize the form
    rate_movie_form = RateMovieForm()

    if rate_movie_form.validate_on_submit():
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        # Update the movie rating and review in the database
        movie_to_update.rating = rate_movie_form.rating.data
        movie_to_update.review = rate_movie_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=rate_movie_form, movie=retrieve_movie)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    result = db.session.execute(db.select(Movie).where(Movie.id == movie_id))
    movie_to_delete = result.scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
