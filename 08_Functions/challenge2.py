import csv
"""
Challenge 2:
"""


# Given the following code
with open("movies.csv", encoding="utf-8") as movie_file:

    for line in csv.reader(movie_file):
        print(line)

"""
TODO 1: Write functions to do the following with the movie data

1. Return a tuple containing the count of tv shows and movies 
2. Given a show_id, return movie data, returned as a dictionary
3. Write a function that can take print show details in a nice format
   You could use keyword parameters and dictionary unpacking
"""


