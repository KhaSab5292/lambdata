"""
utililty functions for working with Dataframes
"""

import pandas as pd
import numpy as np


TEST_DF = pd.DataFrame([1, 2, 3, 4, 5])


def null_check(df):
    """ Checks a dataframe for nulls."""
    null_table = df.isnull().sum()
    return null_table


def find_seconds(d, h, m, s):
   """ Takes in integer number of days, hours, minutes, and seconds. 
   Returns total number of seconds."""
   seconds = 86400*d + 3600*h + 60*m + s
   return seconds