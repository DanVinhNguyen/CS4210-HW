# -------------------------------------------------------------------------
# AUTHOR: Dan Nguyen
# FILENAME: knn.py
# SPECIFICATION: File used to compare the error rate of KNN against other ML algorithms
# FOR: CS 4210- Assignment #2
# TIME SPENT: 6 hrs
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
classes_to_numeric = {"-": 1, "+": 2}
error_total = 0

# reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)


# loop your data to allow each instance to be your test set
for skipped_instance in db:
    # add the training features to the 2D array X removing the instance that will be used for testing in this iteration. For instance, X = [[1, 3], [2, 1,], ...]]. Convert each feature value to
    # float to avoid warning messages
    # --> add your Python code here
    # X =
    X = []


    for i in range(len(db)):
        if db[i] == skipped_instance: # skips the instance
            continue

        temp = []
        for j in range(len(db[i])):
            if j < len(db[i]) - 1: # ignore the last index, for class
                temp.append(float(db[i][j]))

        #print(f'temp: {temp}')
        X.append(temp)

    #print(X)

    # transform the original training classes to numbers and add to the vector Y removing the instance that will be used for testing in this iteration. For instance, Y = [1, 2, ,...]. Convert each
    #  feature value to float to avoid warning messages
    # --> add your Python code here
    # Y =
    Y = []

    for i in range(len(db)):
        if db[i] == skipped_instance: # skips the instance
            continue

        Y.append(float(classes_to_numeric[db[i][-1]]))

    # print(Y)


    # store the test sample of this iteration in the vector testSample
    # --> add your Python code here
    # testSample =
    testSample = []

    for i in range(len(skipped_instance)):
        if i != len(skipped_instance) - 1:
            testSample.append(float(skipped_instance[i]))
        else:
            testSample.append(float(classes_to_numeric[skipped_instance[i]]))


    # fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    # use your test sample in this iteration to make the class prediction. For instance:
    # class_predicted = clf.predict([[1, 2]])[0]
    # --> add your Python code here
    class_predicted = clf.predict([testSample[0:2]])[0]

    # compare the prediction with the true label of the test instance to start calculating the error rate.
    # --> add your Python code here
    if testSample[2] != class_predicted:
        error_total += 1

# print the error rate
# --> add your Python code here
print(f"Error Rate: {error_total / len(db)}")