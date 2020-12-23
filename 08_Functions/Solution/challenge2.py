"""
Challenge 2:
"""

"""
Process the CSV movie file

To process movies.csv 
You could:
Read the file in a for loop and use the split function
to split by commas. That might not work well enough because some of the text fields have commas!

So try using the csv module to complete the ToDo's below.
You will probably need to google it :)
Just like the real world! (We google a lot!)

"""

# We give you the following code to do with as you will
# movie_files = open("movies.csv")

"""
TODO 2: Write functions to do the following

1. Return a tuple containing the count of tv shows and movies 
2. Given a show_id, return movie data, returned as a dictionary
3. Write a function that can take print show details in a nice format
   You could use keyword parameters and dictionary unpacking
"""

import csv


def report_show_splits():
    count = 0
    tv = 0
    movie = 0

    for line in csv.reader(open("movies.csv")):
        if count > 0:
            tv += 1 if line[1] == "TV Show" else 0
            movie += 1 if line[1] == "Movie" else 0
            count += 1

    return count, tv, movie


def get_movie(show_id):
    show = csv.reader(open("movies.csv"))
    columns = next(show)
    line = [None]
    while line[0] != show_id:
        line = next(show, None)
        if line is None:
            break
    else:
        return {z[0]: z[1] for z in zip(columns, line)}


def print_show_details(header_width=80, **kwargs):
    print("=" * 80)
    for k, y in kwargs.items():
        print(f"{k.capitalize()}: {y}")
    print("=" * 80)


if __name__ == '__main__':
    import functools as f
    import pandas as pd

    report_show_splits()
    df = pd.read_csv("movies.csv")
    print(df.groupby(["type"])["type"].count()[0:1])

    # print_show_details(**get_movie("80164077"))
    # print((l[1] for l in csv.reader(open("movies.csv"))))