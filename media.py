import webbrowser

class Media():
    ''' Takes as input a title and the url of a poster image for given media
     and provides a way to store media related information'''
    def __init__(self, title, poster_image_url):
        self.title = title
        self.poster_image_url = poster_image_url

class Movie(Media):
    ''' This class provides a way to store movie related information and
    utilizes the Media class as an input to retrive title and poster URL'''
    def __init__(self, title, movie_storyline, poster_image_url,
                trailer_youtube):
        Media.__init__(self, title, poster_image_url)
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TV_Show(Media):
    ''' This class provides a way to store TV Show related information and
    utilizes the Media class as an input to retrive title and poster URL'''
    def __init__(self, title, series_storyline, poster_image_url,
                series_trailer):
        Media.__init__(self, title, poster_image_url)
        self.storyline = series_storyline
        self.series_trailer_url = series_trailer

    def show_trailer(self):
        '''This function will show a specific trailer in a webbrowser taking
        self from the above classes as input'''
        webbrowser.open(self.series_trailer_url)
