# -------------------------------------------------------------------------
# AUTHOR: Dan Nguyen
# FILENAME: decision_tree_2.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: 6 hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
feature_to_numeric = {'Young': 1, 'Myope': 1, 'Normal': 1, 'Yes': 1,
                      'Prepresbyopic': 2, 'Hypermetrope': 2, 'Reduced': 2, 'No': 2,
                      'Presbyopic': 3}


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


for ds in dataSets:
    dbTraining = []
    X = []
    Y = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    # transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    # X =
    for i in range(len(dbTraining)):
        # temporary holder to append to X
        temp = []

        for j in range(len(dbTraining[i])):
            # skips last value
            if j == (len(dbTraining[i]) - 1):
                continue

            if dbTraining[i][j] in feature_to_numeric:
                temp.append(int(feature_to_numeric[dbTraining[i][j]]))
            else:
                temp.append(dbTraining[i][j])

        X.append(temp)
    # print(X)

    # transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> add your Python code here
    # Y =
    for i in range(len(dbTraining)):
        if dbTraining[i][-1] in feature_to_numeric:
            Y.append(feature_to_numeric[dbTraining[i][-1]])
    # print(Y)

    # loop your training and test tasks 10 times here
    lowAcc = 1
    for i in range(10):

        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)

        # read the test data and add this data to dbTest
        # --> add your Python code here
        # dbTest =
        dbTest = []
        with open('contact_lens_test.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for j, row in enumerate(reader):
                if j > 0:  # skipping the header
                    dbTest.append(row)

        X2 = []
        Y2 = []
        for instance in range(len(dbTest)):
            # transform the features of the test instances to numbers following the same strategy done during
            # training, and then use the decision tree to make the class prediction. For instance: class_predicted =
            # clf.predict([[3, 1, 2, 1]])[0] where [0] is used to get an integer as the predicted class label so that
            # you can compare it with the true label --> add your Python code here
            test_features = []
            for element in range(4):
                test_features.append(int(feature_to_numeric[dbTest[instance][element]]))

            X2.append(test_features)

        for instance in range(len(dbTest)):
            if dbTest[instance][4] == 'Yes':
                Y2.append(1)
            else:
                Y2.append(2)

            count = 0

        # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
        # --> add your Python code here
        for instance in range(len(X2)):
            class_predicted = clf.predict([X2[instance]])[0]
            if Y2[instance] == class_predicted:
                count = count + 1
        accuracy = count / len(X2)
        if accuracy < lowAcc:
            lowAcc = accuracy

    # print the average accuracy of this model during the 10 runs (training and test set).
    # your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    # --> add your Python code here
    print(f'Final accuracy when training on {ds}: {lowAcc:.4f}')
