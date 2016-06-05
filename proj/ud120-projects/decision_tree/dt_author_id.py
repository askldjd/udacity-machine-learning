#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

""" compute the accuracy of your Naive Bayes classifier """

print(len(features_train[0]))


from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)

print('classifier training begin')
### fit the classifier on the training features and labels
t0 = time()

clf = clf.fit(features_train, labels_train)

print "training time:", round(time()-t0, 3), "s"


### calculate and return the accuracy on the test data
### this is slightly different than the example,
### where we just print the accuracy
### you might need to import an sklearn module
print('classifier prediction begin')
t0 = time()
clf.predict(features_test)
print "predict time:", round(time()-t0, 3), "s"

accuracy = clf.score(features_test, labels_test)
print(accuracy)
# return accuracy

#########################################################


