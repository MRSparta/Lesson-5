import csv

with open("imdbtitles.csv", newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # for row in csvreader:
    #     print(row)


    for row in csvreader:
        if (row[4] == '2010' or row[4] == '2011' or row[4] == '2012' or row[4] == '2013' or row[4] == '2014'or row[4] == '2015' or row[4] == '2016' or  row[4] == '2017'or row[4] == '2018' or row[4] == '2019')\
                and row[0] == 'movie':
            print(row[1], " made in the year ",row[4])
        elif row[1] =='primaryTitle':
            print("Movie Title")
        else:
            continue



