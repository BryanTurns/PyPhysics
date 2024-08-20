from const import WINDOW_WIDTH, WINDOW_HEIGHT, MAX_INITIAL_VELOCITY
import numpy as np
import random
from time import time
import math

def randomFill(quantity, maxMass):
    random.seed()
    entityList = np.zeros((quantity, 6))
    for entity in entityList:
        entity[0] = random.random() * maxMass
        entity[1] = random.random() * WINDOW_WIDTH
        entity[2] = random.random() * WINDOW_HEIGHT
        entity[3] = random.random() * MAX_INITIAL_VELOCITY - MAX_INITIAL_VELOCITY / 2
        entity[4] = random.random() * MAX_INITIAL_VELOCITY - MAX_INITIAL_VELOCITY / 2


    return entityList 

def randomFillMulti(quantity, maxMass):
    random.seed()
    entityList = np.zeros((quantity, 7))
    for entity in entityList:
        entity[0] = random.random() * maxMass
        entity[1] = random.random() * WINDOW_WIDTH
        entity[2] = random.random() * WINDOW_HEIGHT
        entity[3] = random.random() * MAX_INITIAL_VELOCITY - MAX_INITIAL_VELOCITY / 2
        entity[4] = random.random() * MAX_INITIAL_VELOCITY - MAX_INITIAL_VELOCITY / 2
        entity[6] = math.floor(random.random() * 3)
    return entityList

def timer_func(func): 
    # This function shows the execution time of  
    # the function object passed 
    def wrap_func(*args, **kwargs): 
        t1 = time() 
        result = func(*args, **kwargs) 
        t2 = time() 
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s') 
        return result 
    return wrap_func 