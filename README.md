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

How to make changes
------------

1. If you want the different set of movies then you need to go to EntertainmentCenter.py and change the list of movies in movies list
2. We are using the omdb api which is getting the data for us in json format, you can request in xml format by changing the querystring.
3. We are reading the json response and saving the data in set of lists.

How to Contribute
-----------------

Fork `the repository`_ on GitHub to start making your changes to the **master** branch
