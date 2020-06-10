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
from sklearn import svm
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]
#c = [10.0,100.0,1000.0,10000.0]



#predict_no = [10,26,50]
clf = svm.SVC(C = 10000,kernel="rbf")
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
#acc = accuracy_score(pred,labels_test)

print sum(pred==1)
	

#########################################################
### your code goes here ###

#########################################################


