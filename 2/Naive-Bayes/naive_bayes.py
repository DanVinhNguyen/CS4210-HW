# -------------------------------------------------------------------------
# AUTHOR: Dan Nguyen
# FILENAME: naive_bayes.py
# SPECIFICATION: This program uses Naive Bayes probabilistic approach to compare to other ML/AI algorithms
# FOR: CS 4210- Assignment #2
# TIME SPENT: 4 hrs
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

# reading the training data in a csv file
# --> add your Python code here
dbTraining = []
features_to_numeric = {"Sunny": 1, "Hot": 1, "High": 1, "Strong": 1,
                       "Overcast": 2, "Mild": 2, "Normal": 2, "Weak": 2,
                       "Rain": 3, "Cool": 3}
classes_to_numeric = {"Yes": 1,
                      "No": 2}


with open("weather_training.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTraining.append(row)

# transform the original training features to numbers and add them to the 4D array X.
# For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# --> add your Python code here
# X =
X = []
for i in range(len(dbTraining)):
    temp = []
    for j in range(len(dbTraining[i])):
        if j == 0:
            continue
        elif j >= len(dbTraining[i]) - 1:
            continue

        temp.append(features_to_numeric[dbTraining[i][j]])

    X.append(temp)

# transform the original training classes to numbers and add them to the vector Y.
# For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
# Y =
Y = []
for i in range(len(dbTraining)):
    Y.append(classes_to_numeric[dbTraining[i][-1]])


# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the test data in a csv file
# --> add your Python code here
dbTest = []
header = []
with open("weather_test.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTest.append(row)
        else:
            header.append(row)

X2 = []
for i in range(len(dbTest)):
    temp = []
    for j in range(len(dbTest[i])):
        if j == 0:
            continue
        elif j >= len(dbTest[i]) - 1:
            continue

        temp.append(features_to_numeric[dbTest[i][j]])

    X2.append(temp)


# printing the header as the solution
# --> add your Python code here
for i in range(len(header[0])):
    print(header[0][i], end = "\t\t")
print()

# use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
# --> add your Python code here
for i in range(len(dbTest)):
    score_yes, score_no = clf.predict_proba([X2[i]])[0]

    if score_yes >= 0.75: # skips the number if both of the scores are below 0.75
        for j in range(len(dbTest[i]) - 1): # sub-index into the instance
            print(dbTest[i][j], end = "\t\t")
        print(f"Yes   (confidence): {score_yes}", end = "\t\t")
        print()
    elif score_no >= 0.75:
        for j in range(len(dbTest[i]) - 1): # sub-index into the instance
            print(dbTest[i][j], end = "\t\t")
        print(f"No   (confidence): {score_no}", end = "\t\t")
        print()
