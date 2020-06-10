#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    #get size of data
    s = len(predictions)
    errors = (net_worths - predictions) **2    
   
    ### store three type of data into tuple, and sorted tuple based on error which is tuple[2][0] and return first 81
    cleaned_data = sorted([(age[0],net_worth[0],error[0]) for age,net_worth,error in zip(ages,net_worths,errors)],key = lambda tup: tup[2])[:int(s*0.9)]
    #cleaned_data.sort(key = lambda tup: tup[2])
    #cleaned_data = cleaned_data[:int(s*0.9)]
    return cleaned_data

