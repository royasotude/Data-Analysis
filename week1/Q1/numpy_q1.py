import numpy as np 
def replace_odd(arr):
    arr = np.asarray(arr)
    output = np.where(arr % 2 == 1 , -1 , arr)
    return output