import csv

for line in csv.reader(open("movies.csv")):

    print(len(line))