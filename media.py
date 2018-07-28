# importing webbrowser module to open the browser window for trailer

import webbrowser


class Movie():

        """ this class provides a way to store movie related information"""

        # valid ratings is a constant variable for all instances

        VALID_RATINGS = ["G", "PG", "PG-13", "R"]
        # init method is a constructor that initializes the data.
        # self is the instance.

        def __init__(self, movie_title, movie_duration, movie_release_date,
                     movie_storyline, movie_director, poster_image,
                     trailer_youtube, movie_rating):
                self.title = movie_title
                self.duration = movie_duration
                self.release_date = movie_release_date
                self.storyline = movie_storyline
                self.director = movie_director
                self.poster_image_url = poster_image
                self.trailer_youtube_url = trailer_youtube
                self.rating = movie_rating

        # show _trailer method will show the trailer from youtube link of movie
        # class
        # input is self(instance).

        def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
