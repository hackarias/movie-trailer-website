import urllib
import json
import webbrowser

__author__ = 'zack'

class Movie():
    """
    This class stores movie related information.
    """
    def __init__(self, movie_title, trailer_youtube):
        """
        Takes a movie title and runs it through an imdb api: http://www.omdbapi.com/ that returns a json file
        with info about the movie. The movies title, plot, poster image, age-rating, duration, imdb ratings and
        awards is then parsed and stored in instance variables.

        Takes a YouTube link for the trailer as well.

        :param movie_title:
        :param trailer_youtube:
        :return:
        """
        connection = urllib.urlopen("http://www.omdbapi.com/?t=" + movie_title)
        movie_info = json.loads(connection.read())

        self.title = movie_info['Title']
        self.storyline = movie_info['Plot']
        self.poster_image_url = movie_info['Poster']
        self.trailer_youtube_url = trailer_youtube
        self.rated = movie_info['Rated']
        self.runtime = movie_info['Runtime']
        self.imdb_rating = movie_info['imdbRating']
        self.awards = movie_info['Awards']

    def show_trailer(self):
        """
        Constructor that opens the youtube trailer.

        :return:
        """
        webbrowser.open(self.trailer_youtube_url)