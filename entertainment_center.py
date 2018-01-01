import media
import fresh_tomatoes

'''The data below is a list of movies and TV shows to be imported into
fresh_tomatoes.py to generate a dynamic webpage. The data calls a class from
media.py which is imported above, along with fresh_tomatoes.py to pass data
to fresh_tomatoes.py'''
toy_story = media.Movie(
'Toy Story',
'A story of a boy and his toys that come to life',
'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
'https://www.youtube.com/watch?v=KYz2wyBy3kc')

avatar = media.Movie(
'Avatar',
'A marine on an alien planet',
'https://www.movieposter.com/posters/archive/main/98/MPW-49246',
'https://www.youtube.com/watch?v=cRdxXPV9GNQ')

saving_private_ryan = media.Movie(
'Saving Private Ryan',
'Matt Damon is being saved again by america, who rah',
'https://images-na.ssl-images-amazon.com/images/I/7132RMjQwjL._RI_.jpg',
'https://www.youtube.com/watch?v=zwhP5b4tD6g')

jurassic_park = media.Movie(
'Jurassic Park',
'A movie about how fucked people would be if dinosaurs were alive',
'https://images-na.ssl-images-amazon.com/images/I/41Iwrrga6rL.jpg',
'https://www.youtube.com/watch?v=Bim7RtKXv90')

dunkirk = media.Movie(
'Dunkirik',
'''A movie about the start of WW2, while British soliders try to escape the
Nazis''',
'https://goo.gl/Pi7Xuy',
'https://www.youtube.com/watch?v=F-eMt3SrfFU')

arrival = media.Movie(
'Arrival',
'''A movie about mysterious crafts that land on earth and how to communicate
with their occupants''',
'https://goo.gl/cBJ4hP',
'https://www.youtube.com/watch?v=tFMo3UJ4B4g')

rick_and_morty = media.Movie(
'Rick and Morty',
'Series about a scientist grandfather and his adventures with his grandson',
'https://goo.gl/TB98b8',
'https://youtu.be/Bmg2vXOQ3kM')

archer = media.Movie(
'Archer',
'Animated series about a spy agency',
'https://goo.gl/BXsYMG',
'https://www.youtube.com/watch?v=ctLSMnaUh4Q')

the_expanse = media.Movie(
'The Expanse',
'''A show set in the near future that follows the crew of the Canterbury,
and a lone detective as they try to solve a mystery and prevent the solar
system from heading toward all-out war.''',
'https://goo.gl/2nzDAi',
'https://www.youtube.com/watch?v=_vPLC2xKGTs')


# The data above is turned into lists below
movies = [toy_story, avatar, jurassic_park, saving_private_ryan, dunkirk,
arrival]

tv_shows = [rick_and_morty, archer, the_expanse]


'''The above lists are now passed into a function from from fresh_tomatoes.py
to generate a dynamic webpage'''
fresh_tomatoes.open_movies_page(movies, tv_shows)
