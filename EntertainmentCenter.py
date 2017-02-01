import Media
import fresh_tomatoes
import urllib
import json

#list of movies to be called from api
movies = ['avatar', 'the dark knight rises', 'the shawshank redemption', 'fight club', 'star wars', '127 hours']
#Empty list is made to be used
title = []
plot = []
imgurl = []
i = 0
#while loop is called to call the api for every movie
while i < len(movies):
    #it opens the url
    jsonurl = urllib.urlopen("http://www.omdbapi.com/?t="+movies[i]+"&y=&plot=short&r=json")
    #gets the response in the text
    text = json.loads(jsonurl.read())
    #appends the response in the list
    title.append(text[u'Title'])
    plot.append(text[u'Plot'])
    imgurl.append(text[u'Poster'])
    i += 1
#conection closed
jsonurl.close()
#object is being created, Movie is being called which is initializing the values to the new object
avatar = Media.Movie(title[0], plot[0],imgurl[0]                        
                        ,"https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_dark_knight_rises = Media.Movie(title[1], plot[1],imgurl[1]
                     ,"https://www.youtube.com/watch?v=g8evyE9TuYk")

the_shawshank_redemption = Media.Movie(title[2], plot[2],imgurl[2]
                                 ,"https://www.youtube.com/watch?v=6hB3S9bIaco")

fight_club = Media.Movie(title[3], plot[3],imgurl[3]
                    ,"https://www.youtube.com/watch?v=SUXWAEX2jlg")

star_wars = Media.Movie(title[4], plot[4],imgurl[4]
                     ,"https://www.youtube.com/watch?v=zv0u8ztv8DA")

one27_hours = Media.Movie(title[5], plot[5],imgurl[5]
                     ,"https://www.youtube.com/watch?v=OlhLOWTnVoQ")
#list of object is created
movies = [avatar, the_dark_knight_rises, the_shawshank_redemption, fight_club, star_wars, one27_hours]
#object are passed in a function
fresh_tomatoes.open_movies_page(movies)
