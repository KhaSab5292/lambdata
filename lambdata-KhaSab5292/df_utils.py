"""
utililty functions for working with Dataframes
"""

import pandas 
import numpy
from sklearn.model_selection import train_test_split

TEST_DF = pandas.DataFrame([1,2,3,4,5])

def null_check(df):
    null_table = df.isnull().sum()
    return null_table
    
def train_val_test(df, train_size, val_size, test_size):
    assert train_size + val_size + test_size == 1 
    
    train, test = train_test_split(df, train_size = train_size + val_size, test_size = test_size,
			           random_state = 42)
    train, val = train_test_split(train, train_size = train_size, test_size = val_size,
			          random_state = 42)
    return train, val, test