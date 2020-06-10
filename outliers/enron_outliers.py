#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop('TOTAL',0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

## people has bonus at least 5M and salary 1M
name =sorted([(k,data_dict[k]['salary'],data_dict[k]['bonus'])for k in data_dict.keys() if data_dict[k]['salary'] != 'NaN'],key = lambda tup:tup[1])[-2:]
       
print name 
### your code below
for point in data:
    salary = point[0]
    bonus = point[-1]
    matplotlib.pyplot.scatter(salary,bonus)
    
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


