#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score
X_train,X_test,y_train,y_test = train_test_split(features,labels,test_size = 0.3,random_state = 42)
clf = DecisionTreeClassifier()
clf.fit(X_train,y_train)
pred = clf.predict(X_test)
# How many POIs are predicted for the test set for your POI identifier?
print "Totoal POIs is ", sum(y_test)

#How many people total are in your test set?
print "Total people is ",len(y_test)

#If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?
print "Accuray of non-POIs is ", (1.0 - sum(y_test)/len(y_test))

#Do you get any true positives? TP == (Acutual label = predict)
TP = [(p,r) for p,r in zip(pred,y_test) if p ==1 and r ==1]
print "The number of TP is ", len(TP)

# Precision
print "Precision is ", precision_score(y_test,pred)
# Recall
print "Recall is :", recall_score(y_test,pred)
#