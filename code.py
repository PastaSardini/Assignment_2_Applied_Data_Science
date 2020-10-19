import pandas as pd

def proportion_of_education():
    # your code goes here
    #proportion of children who had a mother with the education levels equal to <12, 12, >12 (no degree), and >12 (with degree)
    df = pd.read_csv("assets/NISPUF17.csv")
    #grab the column of the csv file of EDUC1 as per document suggests that this is the correct column
    educ = df['EDUC1']
    #calculate the count with this function and normalize each value against the total, sort them respectively)
    x= educ.value_counts(normalize = True, sort=True)
    #define a new dictionary with keys set above
    proportion_of_education = {'less than high school': [],'high school': [], 'more than high school but not college': [],'college': []}
    #append new values to new dictionary with the append function
    proportion_of_education['less than high school'].append(x[1])
    proportion_of_education['high school'].append(x[2])
    proportion_of_education['more than high school but not college'].append(x[3])
    proportion_of_education['college'].append(x[4])
    return proportion_of_education
# YOUR CODE HERE
    raise NotImplementedError()