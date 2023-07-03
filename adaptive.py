# HERE, WE WILL START BY IMPORTING LIBRARIES 

import numpy as np
from heapq import heappush, heappop, heapify

from A_star import *
from utilizations import *

def adaptive_implementation(setup_plot, input_grid_size,plotting):
    """This function implements the adaptive A* algorithm 

    Args:
        setup_plot (tuple): It is the environment(Environment grid, source node, destination node)
        input_grid_size (int): It is the input grid size
        plot (bool): To show whether the function needs to plot the graph or not

    Returns:
        int: It returns the number of expanded cells
    """    
    setup , source_node, destination_node = setup_plot
    g = np.full((input_grid_size+2, input_grid_size+2),np.inf)
    g_traversed = np.full((input_grid_size+2, input_grid_size+2),np.inf)
    f = np.full((input_grid_size+2, input_grid_size+2),np.inf)
    h = hgrid(input_grid_size,destination_node)

    grid_agent = np.full((input_grid_size, input_grid_size),2)
    grid_agent = np.pad(grid_agent, [(1, 1), (1, 1)], mode='constant')
    grid_agent[source_node] = 3
    grid_agent[destination_node] = 4
    extra_counter = 0

    node = source_node
    counter = 0

    while(node!= destination_node):
        
        prev_node= astar_implementation(grid_agent,node,destination_node,h,g,f,g_traversed)
        extra_counter += np.isfinite(g_traversed).sum()

        if prev_node == False:
            print("THIS PATH IS NOT POSSIBLE FOR THE AGENT TO TRAVERSE!")
            break

        path = trajectory(prev_node,node,destination_node)

        while(node!= destination_node):
            
            counter += 1
            mode = 'ADAPTIVE A*'
            
            if plotting == True:
                show_trajectory(grid_agent,node,counter,mode,setup,h,g_traversed,path)

            next_node = path.pop(0)
            show_route(node,setup,grid_agent)

            if grid_agent[next_node] == 0:

                g_traversed[g_traversed == np.inf] = 0
                g_traversed[g_traversed != 0] = g_traversed[destination_node] - g_traversed[g_traversed != 0]
                h[g_traversed != 0 ] = g_traversed[g_traversed != 0]

                g_traversed = np.full((input_grid_size+2, input_grid_size+2),np.inf)
                g = np.full((input_grid_size+2, input_grid_size+2),np.inf)
                f = np.full((input_grid_size+2, input_grid_size+2),np.inf)
                
                break
            node = next_node
        if node == destination_node and plotting == True:
            print("THE AGENT HAS REACHED THE DESTINATION NODE!")

    return extra_counter
        
    # CHECK THE enviroment_set and where it was used  
    #adaptive_implementation(Environment_set[36],input_grid_size,map = True)