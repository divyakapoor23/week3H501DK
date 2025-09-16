
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
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fib(n-1) + fib(n-2)
print("Fibonacci Sequence:")
print(fib(10))
print(fib(14))
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
def taski():
    missing_count = df_bellevue.isnull().sum()
    sorted_columns = missing_count.sort_values().index.tolist()
    print(sorted_columns)


"""Calculate the total number of admissions per year and return a DataFrame with 'Year' and 'Total_Admissions
"""
def taskii():
    
    df_bellevue['date_in'] = pd.to_datetime(df_bellevue['date_in'], errors='coerce')
    df_bellevue['Year'] = df_bellevue['date_in'].dt.year
    df_yearly = df_bellevue.groupby('Year').size().reset_index(name='Total_Admissions')
    print(df_yearly)


"""
Calculate the average age of patients grouped by gender
"""
def taskiii():
    avg_age_by_gender = df_bellevue.groupby('gender')['age'].mean().reset_index(name='avg_age')
    print(avg_age_by_gender)


""" 
    Identify the top 5 most common professions among the patients
"""
def taskiv():
    # 
    top5_professions = df_bellevue['profession'].value_counts().head(5).index.tolist()
    print(top5_professions)

print("Results for Exercise 3:")
print(taski())
print(taskii())
print(taskiii())
print(taskiv())
