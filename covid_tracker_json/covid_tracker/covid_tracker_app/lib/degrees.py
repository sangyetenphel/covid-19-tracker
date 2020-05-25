import csv
import sys
import os
import json

from .util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
with open('covid_tracker_app/db/names.json') as f:
    names = json.load(f)

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
with open('covid_tracker_app/db/people.json') as f:
    people = json.load(f)

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
with open('covid_tracker_app/db/movies.json') as f:
    movies = json.load(f)



def trace(source, target):
    # Get the id of person name

    if source.isdigit() and target.isdigit():
        pass
    elif source.isdigit():
        target = person_id_for_name(target)
    elif target.isdigit():
        source = person_id_for_name(source)
    else:
        source = person_id_for_name(source)
        target = person_id_for_name(target)

    if source == None or target == None:
        return "None"
    if type(source) == list:  
        return source
    elif type(target) == list:
        return target

    path = shortest_path(source, target)

    if path is None or path == []:
        return "Not connected"
    else:
        degrees = len(path)
        chances = chances_cal(degrees)
        path = [(None, source)] + path
        traced = {'degrees': degrees, 'path': [], 'chances': chances}
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            traced['path'].append([person1, person2, movie])
        traced['target'] = person2
        return traced


def chances_cal(degrees):
    """
    Return the chances of contracting 
    """
    chances = 100
    for i in range(1, degrees):
        chances -= 10
    return chances
    

def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.
    If no possible path, returns None.
    """ 
    # Create a node with source as the initial state
    start = Node(state=source, parent=None, action=None) 

    # Creating a empty queue frontier aka BFS
    frontier = QueueFrontier()

    # Adding the initial state to the frontier
    frontier.add(start)  

    # Initialize an empty unexplored state
    explored_state = set()

    while True:
        if frontier.empty():
            return None 
        
        # Remove a node from the frontier 
        current_node = frontier.remove()
        
        if current_node.state == target:
            path = []

            while current_node.parent is not None:
                path.append((current_node.action, current_node.state))
                current_node = current_node.parent

            path.reverse()
            
            return path

        explored_state.add(current_node)


        # A set of tuple of all the movies the current person is in and all stars starred in that movie
        for movie, person in neighbors_for_person(current_node.state):
            if not frontier.contains_state(person) and person not in explored_state:

                new_node = Node(state=person, parent=current_node, action=movie)
                if new_node.state == target:
                    path = []

                    while new_node.parent is not None:
                        path.append((new_node.action, new_node.state))
                        new_node = new_node.parent

                    path.reverse()
                    return path

                frontier.add(new_node)


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        same_name = []
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            same_name.append(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        return same_name
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()