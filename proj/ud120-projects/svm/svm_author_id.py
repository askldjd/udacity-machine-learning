#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

from sklearn.svm import SVC
from sklearn.externals import joblib

# C = 10000 is optimized following training course. 10,100,1000 were tried as well.
clf = SVC(kernel="rbf", C=10000)
retrain = False
try:
    clf = joblib.load('clf.pki')
except:
    print('Need to retrain');
    retrain = True

# slice the array to 1% since RBF is so slow
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

### fit the classifier on the training features and labels
if retrain == True:
    t0 = time()
    clf.fit(features_train, labels_train)
    joblib.dump(clf, 'clf.pki')
    print "training time:", round(time()-t0, 3), "s"


### calculate and return the accuracy on the test data
### this is slightly different than the example,
### where we just print the accuracy
### you might need to import an sklearn module
t0 = time()
pred = clf.predict(features_test)
print(pred[10], pred[26], pred[50])
print "predict time:", round(time()-t0, 3), "s"

print(pred.tolist().count(1))
print(pred.tolist().count(0))

accuracy = clf.score(features_test, labels_test)
print(accuracy)
#########################################################


