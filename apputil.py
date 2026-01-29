import numpy as np


def ways(n):
    """
    Return the number of ways to represent n cents using only nickels.

    Parameters:
        n (int): Amount in cents

    Returns:
        int: Number of possible ways
    """
    count = 0
    for _ in range(n // 5 + 1):
        count += 1
    return count


def lowest_score(names, scores):
    """
    Return the name of the student with the lowest test score.

    Parameters:
        names (np.ndarray): Array of student names
        scores (np.ndarray): Array of test scores

    Returns:
        str: Name of the student with the lowest score
    """
    lo_s = np.argmin(scores)
    return names[lo_s]


def sort_names(names, scores):
    """
    Return student names sorted in descending order of test score.

    Parameters:
        names (np.ndarray): Array of student names
        scores (np.ndarray): Array of test scores

    Returns:
        np.ndarray: Names sorted from highest to lowest score
    """
    na_s = np.argsort(scores)[::-1]
    return names[na_s]


if __name__ == "__main__":
    # Simple test cases
    names = np.array(["Hannah", "Astrid", "Abdul", "Mauve", "Jung"])
    scores = np.array([99, 71, 85, 62, 91])

    print(ways(25))
    print(lowest_score(names, scores))
    print(sort_names(names, scores))
