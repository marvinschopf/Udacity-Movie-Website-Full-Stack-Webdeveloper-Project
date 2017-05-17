import webbrowser

class Movie():
    # Initialise the Movie Class
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_language):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.language = movie_language

    # Show Trailer function, it opens the trailer in a Browser
    def show_trailer(self):
        print("Playing trailer of",self.title,"in webbrowser!")
        webbrowser.open(self.trailer_youtube_url)
