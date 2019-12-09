"""
utililty functions for working with Dataframes
"""

import pandas 
import numpy

TEST_DF = pandas.DataFrame([1,2,3,4,5])

def null_check(df):
    return df.isnull().sum()
