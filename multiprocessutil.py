import numpy as np
import multiprocessing as mp


def to_shared_array(arr, ctype):
    shared_array = mp.Array(ctype, arr.size, lock=False)
    temp = np.frombuffer(shared_array, dtype=arr.dtype)
    temp[:] = arr.flatten(order='C')
    return shared_array

def to_numpy_array(shared_array, shape):
    '''Create a numpy array backed by a shared memory Array.'''
    arr = np.ctypeslib.as_array(shared_array)
    return arr.reshape(shape)

def check_status(shared_array, shape, lock, process_number):
    status_array = to_numpy_array(shared_array, shape)

    # Ensure that all status elements are set to 0
    while True:
        for status in status_array:
            if status == 1:
                continue
        break