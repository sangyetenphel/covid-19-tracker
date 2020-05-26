# covid-19-tracker
Use AI to track COVID-19 contraction chances in Hollywood

Given an actor name, the app traces down and tries to find a connection to another actor who has been tested positive for COVID-19. 
This can be treated as an AI search problem where we are trying to find the shortest path between 2 actors.
Our states are people. Our actions are movies, which take us from one actor to another.
Our initial state and goal state are defined by the two people we’re trying to connect.
By using breadth-first search, we can find the shortest path from one actor to another.


The app also shows the latest Coronavirus cases in the U.S.
For this I used a python web scraper i.e. BeautifulSoup4 to scape data from the source: https://www.worldometers.info/coronavirus/country/us/

Finally, I generate some random facts about the virus on the botton left section which changes on every http request made.
