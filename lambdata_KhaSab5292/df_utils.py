"""
utililty functions for working with Dataframes
"""

import pandas as pd
import numpy as np


TEST_DF = pd.DataFrame([1, 2, 3, 4, 5])


def null_check(df):
    """Checks a dataframe for nulls."""
    null_table = df.isnull().sum()
    return null_table


def list_to_df(df, the_list, name):
    """Turns a list into a series and then adds it under a given
    name to a given dataframe"""
    new_column = pd.Series(the_list)
    df[name] = new_column
    return df


def find_seconds(d, h, m, s):
    """Takes in integer number of days, hours, minutes, and seconds.
    Returns total number of seconds."""
    seconds = 86400*d + 3600*h + 60*m + s
    return seconds

class Grade:
    def __init__(self, number=50):
        self.number = number
        
    def letter(self):
        percent = self.number/100
        if percent > 1:
            return "Not possible"
        elif percent >= .9:
            return "A"
        elif percent >= .8:
            return "B"
        elif percent >= .7:
            return "C"
        elif percent >= .6:
            return "D"
        else:
            return "F"
    
