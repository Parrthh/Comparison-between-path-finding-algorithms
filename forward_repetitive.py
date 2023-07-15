# HERE, WE WILL START BY IMPORTING LIBRARIES

import numpy as np
import random
import matplotlib.pyplot as plt
import time
from heapq import heappush, heappop, heapify
import pandas as pd

from A_star import *
from utilizations import *



def forward_repetitive(setup_plot, input_grid_size, plot):
    """ This function implements the repetitive forward A* algorithm 

    Args:
        setup_plot (tuple): It is the environment(Environment grid, source node, destination node)
        input_grid_size (int): It is the input grid size
        plot (bool): To show whether the function needs to plot the graph or not

    Returns:
        int: It returns the number of expanded cells
    """    
    setup , source_node , destination_node = setup_plot
    g = np.full((input_grid_size+2, input_grid_size+2),np.inf)
    g_traversed = np.full((input_grid_size+2, input_grid_size+2),np.inf)
    f = np.full((input_grid_size+2, input_grid_size+2),np.inf)
    h = hgrid(101,destination_node)

    expanded_counter = 0

    grid_agent = np.full((input_grid_size, input_grid_size),2)
    grid_agent = np.pad(grid_agent, [(1, 1), (1, 1)], mode='constant')
    grid_agent[source_node] = 3
    grid_agent[destination_node] = 4

    counter = 0
    node = source_node

    while(node!= destination_node):
        curr_source_node = node
        prev_node = astar_implementation(grid_agent,node,destination_node,h,g,f,g_traversed)
        expanded_counter += np.isfinite(g_traversed).sum()

        if plot == True:
            astar_plotting(grid_agent,g_traversed,curr_source_node,destination_node,prev_node)

        if prev_node == False:
            print("THIS PATH IS NOT POSSIBLE FOR THE AGENT TO TRAVERSE!")
            break
        
        path = trajectory(prev_node,curr_source_node,destination_node)
        
        while(node!=destination_node):
            counter+=1
            category = 'REPEATED FORWARD A*'
            
            if plot == True:
                show_trajectory(grid_agent,node,counter,category,setup,h,g_traversed,path)
            
            next_node = path.pop(0)
            show_route(node,setup,grid_agent)

            if grid_agent[next_node] == 0:
                
                grid_agent[next_node] = 0
                g = np.full((input_grid_size+2, input_grid_size+2),np.inf)
                f = np.full((input_grid_size+2, input_grid_size+2),np.inf)
                g_traversed = np.full((input_grid_size+2, input_grid_size+2),np.inf)
                break

            node = next_node
            
    if node == destination_node and plot == True:
        print("THE AGENT HAS REACHED THE DESTINATION NODE")
    
    return expanded_counter

