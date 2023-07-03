# HERE, WE WILL START BY IMPORTING LIBRARIES 

import numpy as np
import random
import matplotlib.pyplot as plt
import time
from heapq import heappush, heappop, heapify
import pandas as pd

from A_star import *


def grid_implementation(input_grid_size):
    input_grid_size = input_grid_size
    setup = np.ones((input_grid_size,input_grid_size))
    setup = np.pad(setup, [(1,1),(1,1)], mode = 'constant')

    return setup

def create_setup(setup, i , j , input_grid_size):
    itr1 = True
    setup[(i , j)] = 2
    stk = [(i , j)]
    mark = set()

    while stk:

        vertex = stk.pop()
        if vertex in mark:
            continue
        x , y = vertex
        if itr1 == False:
            setup[x,y] = int(np.random.choice([0, 2], size=(1,1), p=[0.3, 0.7]))
        else:
            itr1 = False
        
        mark.add(vertex)
        preceed_nodes = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
        np.random.shuffle(preceed_nodes)
        preceed_nodes = [(m,n) for (m,n) in preceed_nodes if m > 0 and n> 0 and m < input_grid_size + 1 and n < input_grid_size + 1]

        for (x,y) in preceed_nodes:
            stk.append((x,y))
    
    return setup


def nodes(setup, input_grid_size):
    p,q = 0,0
    while setup[p,q]== 0:
        (p,q) = (random.randint(1, input_grid_size),random.randint(1, input_grid_size))

    setup[p,q] = 3
    source_node = (p,q)
    p,q = 0,0
    while setup[p,q] == 0:
        (p,q) = (random.randint(1,input_grid_size),random.randint(1, input_grid_size))
    setup[p,q] = 4
    destination_node = (p,q)
    setup[ input_grid_size + 1, input_grid_size + 1] = 6

    return (setup, source_node, destination_node)

def number_setups(no_setups, input_grid_size):
    setup_env = []
    for number in range(no_setups):
        arr = grid_implementation(input_grid_size)
        (p,q) = (random.randint(1,input_grid_size),random.randint(1, input_grid_size))

        setup = create_setup(arr,p,q,input_grid_size)
        nodes_in_setup = nodes(setup, input_grid_size)
        setup_env.append(nodes_in_setup)
    return setup_env



