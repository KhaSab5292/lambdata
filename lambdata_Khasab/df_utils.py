"""
utililty functions for working with Dataframes
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


TEST_DF = pd.DataFrame([1, 2, 3, 4, 5])


def null_check(df):
    """ Checks a dataframe for nulls."""
    null_table = df.isnull().sum()
    return null_table


def train_val_test(df, train_size, val_size, test_size):
    assert train_size + val_size + test_size == 1

    train, test = train_test_split(df, train_size=train_size + val_size,
                                   test_size=test_size, random_state=42)
    train, val = train_test_split(train, train_size=train_size,
                                  test_size=val_size, random_state=42)
    return train, val, test


def find_seconds(d, h, m, s):
   """ Takes in integer number of days, hours, minutes, and seconds. 
   Returns total number of seconds."""
   seconds = 86400*d + 3600*h + 60*m + s
   return seconds