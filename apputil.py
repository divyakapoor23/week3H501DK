
import pandas as pd
import numpy as np  

## function 1
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fib(n-1) + fib(n-2)

## function 2
def to_binary(n):
    """Convert a decimal number to its binary representation."""
    if n < 0:
        return "Input should be a non-negative integer."
    # Using Python's built-in bin function to convert decimal to binary
    # and remove the '0b' prefix
    return bin(n).replace("0b", "")


url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)
df_bellevue.head()

## function 4
def taski():
    missing_count = df_bellevue.isnull().sum()
    sorted_columns = missing_count.sort_values().index.tolist()
    print(sorted_columns)


def taskii():
    # Suppose your date column is named 'date'
    # df_bellevue['date_in'] = pd.to_datetime(df_bellevue['date_in'], errors='coerce')
    # df_bellevue['year'] = df_bellevue['date_in'].dt.year
    # df_bellevue['month'] = df_bellevue['date_in'].dt.month
    # df_bellevue['day'] = df_bellevue['date_in'].dt.day
    # print(df_bellevue[['date', 'year', 'month', 'day']].head())
    # df_bellevue['date_in'] = pd.to_datetime(df_bellevue['date_in'])
    df_bellevue['Year'] = df_bellevue['date_in'].dt.year
    df_yearly = df_bellevue.groupby('Year').size().reset_index(name='Total_Admissions')
    print(df_yearly)

def taskiii():
    avg_age_by_gender = df_bellevue.groupby('gender')['age'].mean().reset_index(name='avg_age')
    print(avg_age_by_gender)

def taskiv():
    top5_professions = df_bellevue['profession'].value_counts().head(5).index.tolist()
    print(top5_professions)


taski()
taskii()
# taskiii()
# taskiv()