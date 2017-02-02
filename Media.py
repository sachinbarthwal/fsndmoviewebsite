import webbrowser


class Movie():
    """The class provides a way to store information of movies"""
    VALID_RATINGS = ["G", "PG", "PG13", "R"]
    """
    A constructor is being called when movie object is created
    and then the value provided in object are initialized here
    """
    def __init__(self, movie_title, movie_storyline,
    poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
# This functions open the provided URL in Browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

