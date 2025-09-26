
import pandas as pd
import numpy as np  

""" 
Load the Bellevue Almshouse dataset
"""
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)
df_bellevue.head()


"""
Fibonacci sequence starting with 0 and 1
"""
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fibonacci(n-1) + fibonacci(n-2)
print("Fibonacci Sequence:")
print(fibonacci(10))
print(fibonacci(14))
"""
Convert a decimal number to its binary representation
"""
def to_binary(n):
    if n < 0:
        return "Input should be a non-negative integer."
    # Using Python's built-in bin function to convert decimal to binary
    # and remove the '0b' prefix
    return bin(n).replace("0b", "")
print("Binary Representation:")
print(to_binary(10))
print(to_binary(23))
print(to_binary(256))
"""
Data Analysis on Bellevue Hospital Admissions
"""
"""
Return a list of column names sorted by the number of missing values in ascending order
"""
# 1. Get the original column order indices
original_order = {col: i for i, col in enumerate(df_bellevue.columns)}

def task_1():
    rc = [col for col in df_bellevue.columns if col != 'year']
    missing_count = df_bellevue[rc].isnull().sum()

    # Use the original index from the full df_bellevue.columns as the tie-breaker
    sorted_columns = sorted(rc, key=lambda x: (missing_count[x], original_order[x]))
    return sorted_columns


"""Calculate the total number of admissions per year and return a DataFrame with 'Year' and 'Total_Admissions
"""
def task_2():
    df_bellevue['date_in'] = pd.to_datetime(df_bellevue['date_in'], errors='coerce')
    df_bellevue['year'] = df_bellevue['date_in'].dt.year
    df_yearly = df_bellevue.groupby('year').size().reset_index(name='total_admissions')
    return df_yearly
    print(df_yearly)


"""
Calculate the average age of patients grouped by gender
"""
def task_3():
    avg_age_by_gender = df_bellevue.groupby('gender')['age'].mean()
    return avg_age_by_gender
    print(avg_age_by_gender)


""" 
    Identify the top 5 most common professions among the patients
"""
def task_4():
    top5_professions = df_bellevue['profession'].value_counts().head(5).index.tolist()
    return top5_professions
    print(top5_professions) 

print("Results for Exercise 3:")
print(task_1())
print(task_2())
print(task_3())
print(task_4())
