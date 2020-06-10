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
"""
with open("../final_project/final_project_dataset.pkl","r") as pickle_file:
    enron_data = pickle.load(pickle_file)
"""
# number of people
print "Number of people:",len(enron_data)

#number of features per person
#print "features:", sum(map(len,enron_data.values()))/len(enron_data)
print "Features per person:", len(enron_data.values()[0])

#No of POI in E+F
poi_no = 0
for k,v in enron_data.items():
    if v['poi'] == 1:
            poi_no +=1
print "Number of POI in E+F:", poi_no 
            
# POI from name.txt the first two lines is website
names = len(open("../final_project/poi_names.txt", "r").readlines())
print "Number of POI from name text:", names-2

#check "PRENTICE JAMES" total stock value
def check_user(name):
    for k in enron_data.keys():
        if name in k:
            print "True"
check_user("PRENTICE JAMES")
print "James Prentice' stock value:", enron_data["PRENTICE JAMES"]['total_stock_value']

#check "COLWELL WESLEY" from this message to poi
check_user("COLWELL WESLEY")
print "Number of Wesley Colwel email messages:", enron_data["COLWELL WESLEY"]['from_this_person_to_poi']

#check "SKILLING JEFFREY K" stock options exercised
check_user("SKILLING JEFFREY K")
print "Jeffrey K Skilling stock options exercised value:", enron_data["SKILLING JEFFREY K"]['exercised_stock_options']

#Lay, Skilling and Fastow who has best total payment
Names= ['Lay', 'Skilling', 'Fastow']
for name in enron_data.keys():
    for i in Names:
        if i.upper() in name:
            print name,"has total payment:",enron_data[name]['total_payments']

            



            
#find the number of quantified salary and known emails
salaries, emails = [i['salary'] for i in enron_data.values()],[i['email_address'] for i in enron_data.values()]
print "Number of quantified salaries:", len(salaries) - salaries.count('NaN')
print "Number of known emails:", len(emails) - emails.count('NaN')

# no of people have 'NaN' on total_payments in E+F and what is the percentage
no_total_payments = [i['total_payments'] for i in enron_data.values()]
no_nan = len([i for i in no_total_payments if i == 'NaN'])
print 'No of peoople have NaN on total_payments in E+F:',no_nan
print 'The percentage of these people is ',no_nan*100/len(no_total_payments),'%'

# no of people POIs in the E+F dataset have NaN for their total payments and what is the percentage
no_total_pois = len([i['poi'] for i in enron_data.values() if i['poi'] == True])
no_pois = len([ i[pois] for i in enron_data.values() if i['total_payments']== 'NaN' and i['poi'] == True])
print 'No of peoople have NaN on pois in E+F:',no_pois
print 'The percentage of these people is ',no_pois*100/no_total_pois,'%'
