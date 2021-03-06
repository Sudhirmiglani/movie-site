# import statements
from flask import Flask, jsonify, make_response, url_for, render_template, send_from_directory, abort
from movie_creator import fetch_movies
import json

app = Flask(__name__)


# Base route to serve index html
@app.route("/")
def main():
    """renders index page on default route"""
    return render_template('index.html')


# Path to serve js files
@app.route('/js/<path:path>')
def send_js(path):
    """returns js files after fetching from js directory"""
    return send_from_directory('js', path)


# Path to serve css files
@app.route('/css/<path:path>')
def send_css(path):
    """returns css files after fetching from css directory"""
    return send_from_directory('css', path)


# Endpoint to fetch all movies
@app.route('/api/v1/movie', methods=['GET'])
def get_task():
    """ function returns list of movies in json format"""
    movies = fetch_movies()
    # Return not found when movies are empty
    if len(movies) == 0:
        abort(404)
    return json.dumps([movie.__dict__ for movie in movies])


# Root handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    """ makes response to return whenever there is a bad request"""
    return make_response(jsonify({'error': 'Bad request'}), 400)


# Root handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """ makes response to return whenever no endpoint/resource found"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run()
