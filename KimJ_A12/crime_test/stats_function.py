# iterates the age column and calculates the mean and median age.

import pandas as pd

def calculate_mean(df):
    return df['Vict age'].mean()

def calculate_median(df):
    return df['Vict age'].median()

