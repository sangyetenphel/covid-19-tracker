# COVID-19 TRACKER
Use AI to track COVID-19 contraction chances in Hollywood.

### About

Given an actor name, the app traces down and tries to find a connection to another actor who has been tested positive for COVID-19. 
We treat this as an AI search problem where we are trying to find the shortest path between 2 actors.
Our states are people. Our actions are movies, which take us from one actor to another.
Our initial state and goal state are defined by the two people we’re trying to connect.
By using breadth-first search, we can find the shortest path from one actor to another in a database of 1044500 different actors.


The app also shows the latest Coronavirus cases in the U.S.
For this I used a python web scraper i.e. BeautifulSoup4 to scape data from the source: https://www.worldometers.info/coronavirus/country/us/

Finally, I generate some random facts about the virus on the botton left section which changes on every http request made.


### Usage

1. Download the folder 'covid_tracker_large' or 'covid_tracker_json' which uses a JSON file instead of a python dictionary to load the huge dataset of all Hollywood actors from source: https://www.imdb.com/.

2. Cd into the folder where there is a manage.py file in it. Run `<python manage.py runserver>` to open the app in your local browser.

Alternatively you can visit this site for a lite version of the same app but with smaller dataset. https://covidtrackerhollywood.herokuapp.com/


