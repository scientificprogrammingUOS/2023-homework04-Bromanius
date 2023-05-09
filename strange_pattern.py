import numpy as np


# implement the function strange pattern

def strange_pattern(dims):
    arr = np.full(dims, False)
    for i in range(dims[0]):
        for j in range(dims[1]):
            if (i + j) % 3 == 0:
                arr[i, j] = True
    return arr


if __name__ == "__main__":
    pass
