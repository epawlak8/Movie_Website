import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')
#print toy_story.storyline

avatar = media.Movie('Avatar',
                        'A marine on an alien planet',
                        'https://www.movieposter.com/posters/archive/main/98/MPW-49246',
                        'https://www.youtube.com/watch?v=cRdxXPV9GNQ')

jurassic_park = media.Movie('Jurassic Park',
                        'A movie about how fucked people would be if dinosaurs were alive',
                        'http://img.moviepostershop.com/jurassic-park-movie-poster-1992-1020141477.jpg',
                        'https://www.youtube.com/watch?v=Bim7RtKXv90')
#print avatar.storyline
#avatar.show_trailer()

movies = [toy_story, avatar, jurassic_park]

#print media.Movie.__doc__
#print media.Movie.__name__
#print media.Movie.__module__
fresh_tomatoes.open_movies_page(movies)
