import seaborn as sns
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

## function 3
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)
df_bellevue.head()
