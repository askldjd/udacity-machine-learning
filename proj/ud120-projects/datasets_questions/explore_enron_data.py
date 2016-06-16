#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#Wesley Colwell
# James Prentice

print enron_data["COLWELL WESLEY"]

count = 0.0
total = 0.0
for key, value in enron_data.iteritems() :
    if value["poi"] == True:
        if enron_data[key]["total_payments"] == "NaN": 
            #print key, len(value)
            count+=1
        total+=1

print count
print total
print '%.2f'%(count / total)

#print enron_data["SKILLING JEFFREY K"]["total_payments"]
#print enron_data["LAY KENNETH L"]["total_payments"]
#print enron_data["FASTOW ANDREW S"]["total_payments"]
