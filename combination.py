import numpy as np


# implement your function to combine two numpy arrays 

def combination(arr1, arr2, axis=0):
    arr1 = np.squeeze(arr1)
    arr2 = np.squeeze(arr2)
    try:
        return np.append(arr1, arr2, axis=axis)
    except ValueError:
        return "Error: All the input arrays must have same number of dimensions!"


if __name__ == "__main__":
    pass
