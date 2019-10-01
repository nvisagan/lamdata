"""
Utility Functions for working with DataFrames
"""

import pandas as pd
import numpy as np

TEST_DF = pd.DataFrame([1,2,3])

# Function to set notebook display options
def optimaloptions(df):
    with pd.set_option('display.max_rows', 999):
        with pd.set_option('precision', 5):
            print(df)


def nullinfo(df):
	no_of_rows = df.shape[0]  #Get number of rows in the Dataframe
	no_of_nulls = df.isnull().sum() #Get a dataframe containing number of nulls in each columns
	null_notify = pd.DataFrame(no_of_nulls).reset_index() # Creating a Dataframe with Null values information
	null_notify.columns = ['Column Name','No of Nulls'] #Naming the columns of the DataFrame
	null_notify['Nulls percent']=np.round(null_notify['No of Nulls']/no_of_rows,2)#using round function to have only 2 decimal points
#Return to the Dataframe
	return null_notify