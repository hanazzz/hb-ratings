"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!

@app.route('/')
def render_homepage():
    """" Homepage """

    return render_template('homepage.html')


@app.route('/movies')
def render_movies():
    """ Show all movies in database. """

    all_movies = crud.return_all_movies()

    return render_template('all_movies.html', movies=all_movies)


@app.route('/movies/<movie_id>')
def show_movie_details(movie_id):
    """ Show a movie from database. """

    # use movie ID to do query + store as movie
    # do the above by using get_movie_by_id()
    movie = crud.return_all_movies()

    return render_template('movie_details.html', movies=movie)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
