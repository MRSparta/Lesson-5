import csv

with open("user_details.csv", newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    for row in csvreader:
        print(row[3])

    """
    first name and last name"""
    # for row in csvreader:
    #     firstname = row[1]
    #     lastname = row [2]
    #     print(firstname + lastname)
    #     # print(row[1:3])

    """
    Title, first name and last name"""

    # for row in csvreader:
    #     title = row[0]
    #     firstname = row[1]
    #     lastname = row [2]
    #     print(title + firstname + lastname)

    male = 0
    female = 0
    for row in csvreader:
        if row[3] == 'Male':
            male = male + 1
            print(row[3])
        elif row[3] == 'Female':
            female = female + 1
            print(female)
        else


print("there are " + str(male) + " males \n and " + str(female) + " females in the list")

    # for row in csvreader:
    #     firstname = row[1]
    #     lastname = row [2]
    #     print(firstname + lastname)