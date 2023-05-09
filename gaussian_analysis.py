import random

import numpy as np


# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    # delete the NotImplementedError when you write your function.
    if type(loc) is not int and type(loc) is not float:
        return "Error: The parameter loc is no int or float!"
    if type(scale) is not int and type(loc) is not float:
        return "Error: The parameter scale is no int or float!"
    if type(lower_bound) is not int and type(loc) is not float:
        return "Error: The parameter lower_bound is no int or float!"
    if type(upper_bound) is not int and type(loc) is not float:
        return "Error: The parameter upper_bound is no int or float!"
    if lower_bound > upper_bound:
        return "Error: The lower bound is higher than the upper bound!"

    arr = np.random.normal(loc=loc, scale=scale, size=100)
    mask = arr >= lower_bound
    arr = arr[mask]
    mask = arr <= upper_bound
    arr = arr[mask]
    mean = np.mean(arr)
    std = np.std(arr)
    return (mean, std)


if __name__ == "__main__":
    gaussian_analysis(0.5, 0.5, 0, 100)
    pass
