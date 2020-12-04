import csv
for line in open("movies.csv"):
    data = line.split(",")
    print(len(data))