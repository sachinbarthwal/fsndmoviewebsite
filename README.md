Movie Website
=========================
This is a project for full stack nanodegree development course, where we are writing the server side code to show the list of our favourite movies.

OMDB Api is being used to get the data in JSON format.

.. code-block:: python

    >>>while i < len(movies):
        >>>#it opens the url
        >>>jsonurl = urllib.urlopen("http://www.omdbapi.com/?t="+movies[i]+"&y=&plot=short&r=json")
        >>>#gets the response in the text
        >>>text = json.loads(jsonurl.read())
        >>>#appends the response in the list
        >>>title.append(text[u'Title'])
        >>>plot.append(text[u'Plot'])
        >>>imgurl.append(text[u'Poster'])
        >>>i += 1
    
  All the code is available in Media.py and EntertainmentCenter.py

Installation
------------

Just downlaod the files and you'll be able to run the application, as it is a web application so no need to install but there are few Prerequisites

1. You need a browser to run the html
2. If you want to make changes to the code of the application then you need to install python as well

How to run
------------

1. Download the fresh_tomatoes
2. click on fresh_tomatoes.html to run the application

How to use in python
------------

1. Download python from https://www.python.org/downloads/
2. Try to download version 2.7 as these files are coded on 2.7
3. Once downloaded and installed opne IDLE (Its like a command prompt for python)
4. Now press cntrl+o to open the downloaded file.
5. Make sure all the files are at one place/folder.
6. Open EntertainmentCenter.py and press f5 to run it on python.
7. It will call media.py and fresh_tomatoes.py and use their functions.
8. If everything works perfectly you will be landed on browser with movie database website.


How to make changes
------------

1. If you want the different set of movies then you need to go to EntertainmentCenter.py and change the list of movies in movies list
2. We are using the omdb api which is getting the data for us in json format, you can request in xml format by changing the querystring.
3. We are reading the json response and saving the data in set of lists.

How to Contribute
-----------------

Fork `the repository`_ on GitHub to start making your changes to the **master** branch
