import pandas as pd

#checks that the 'Vict sex' column is either M or F and not missing (NULL)
#check the column  'Vict age' that the values are between 1-100 and not missing (NULL)
def validate(df):
    sex = df['Vict sex'].isin(['M', 'F']) & df['Vict sex'].notnull()

    age = df['Vict age'].between(1, 100) & df['Vict age'].notnull()

    if (sex.all() and age.all()):
        return True
    return False
