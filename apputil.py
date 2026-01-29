import numpy as np


# update/add code below ...

def ways(n):
    count = 0
    for nickels in range(n // 5 + 1):
        count += 1
    return count



def lowest_score(names, scores):
    idx = np.argmin(scores)
    return names[idx]


def sort_names(names, scores):
    idx = np.argsort(scores)[::-1]
    return names[idx]