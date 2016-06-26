#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)

for x in data_dict:
    print data_dict[x]['salary'], x
    # for y in cars[x]:
    #     print (y,':',cars[x][y])


### your code below


for point in data:    
    salary = point[0]
    bonus = point[1]
    # print salary, bonus
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.savefig('enron-outlier.png')
