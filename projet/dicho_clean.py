import pandas as pd
from functions import test_bool, test_45int

def dicho_search(value, numbers):
    """
    Search for a value in a list using dichotomous method
    """
    n = len(numbers)
    if n == 1:
        return numbers[0] == value

    mid = n // 2
    if numbers[mid] == value:
        return True
    elif numbers[mid] > value:
        return dicho_search(value, numbers[:mid])
    else:
        return dicho_search(value, numbers[mid:])

def search_by_iteration(tirage, value):
    """
    Search for a value in a DataFrame by iteration
    """
    tirage_drop = pd.DataFrame(columns=tirage.columns)
    j = 0
    for i, row in tirage.iterrows():
        t = row[1:].tolist()
        if dicho_search(value, t):
            tirage_drop.loc[j] = row
            j += 1
    return tirage_drop

def search_by_recursion(tirage, value):
    """
    Search for a value in a DataFrame by recursion
    """
    tirage_drop = pd.DataFrame(columns=tirage.columns)
    j = 0
    for i, row in tirage.iterrows():
        t = row[1:].tolist()
        if dicho_search(value, t):
            tirage_drop.loc[j] = row
            j += 1
    return tirage_drop

def run_dicho(tirage, search, lst):
    """
    Run dichotomous search
    """
    is_recursive = test_bool(input("Which algorithm do you want to use for this search? (0 : iterative, 1 : recursive) : "))
    if search:
        value = test_45int(input("Which number do you want to search in the drawing(s)? (between 1 and 45) : "))
        if is_recursive:
            tirage_drop = search_by_recursion(tirage, value)
        else:
            tirage_drop = search_by_iteration(tirage, value)
        return tirage_drop
    else:
        lst_occurence = []
        for value in lst:
            occurence = 0
            for i, row in tirage.iterrows():
                t = row[1:].tolist()
                if dicho_search(value, t):
                    occurence += 1
            lst_occurence.append(occurence)
        return lst_occurence