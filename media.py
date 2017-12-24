import webbrowser

class Media():
    def __init__(self, title, poster_image_url):
        self.title = title
        self.poster_image_url = poster_image_url

class Movie(Media):
    ''' this class provides a way to store movie related information'''
    def __init__(self, title, movie_storyline, poster_image_url,
                trailer_youtube):
        Media.__init__(self, title, poster_image_url)
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TV_Show(Media):
    ''' this class provides a way to store TV Show related information'''
    def __init__(self, title, series_storyline, poster_image_url,
                series_trailer):
        Media.__init__(self, title, poster_image_url)
        self.storyline = series_storyline
        self.series_trailer_url = series_trailer

    def show_trailer(self):
        webbrowser.open(self.series_trailer_url)
