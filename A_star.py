# HERE, WE WILL START BY IMPORTING LIBRARIES 

import numpy as np
import random
import matplotlib.pyplot as plt
import time
from heapq import heappush, heappop, heapify
import pandas as pd

c = 1

def heuristic_implementation(h, curr_node, destination_node):
    """Here, we are filling the h with its initial heuristic values

    Args:
        h (numpy array): It will contain the heuristic value of each and every node in the grid
        curr_node (tuple): It is the starting node for creating heuristic
        destination_node (tuple): It is a destination node for the heuristic function
    """    
    destination_node_xcoord, destination_node_ycoord = destination_node
    curr_node_xccord , curr_node_ycoord = curr_node
    h[curr_node_xccord, curr_node_ycoord] = abs (destination_node_xcoord - curr_node_xccord) + abs (destination_node_ycoord - curr_node_ycoord)

def hgrid(input_grid_size, destination_node):
    """Here, we are just initialzing the h

    Args:
        input_grid_size (int): To enter the size of the grid
        destination_node (tuple): It is a destination node for the heuristic function

    Returns:
        numpy array: The final created h values
    """    
    h = np.full((input_grid_size + 2, input_grid_size + 2), np.inf)
    partial_nodex = [ x for x in range(1, input_grid_size + 1)]
    partial_nodey = [ y for y in range(1,input_grid_size + 1)]
    itr = []
    for x in partial_nodex:
        for y in partial_nodey:
            heuristic_implementation(h,(x,y), destination_node)
    return h

def adjacent(grid_agent, curr_node, traversed_node):
    """Here, we are getting all the adjacent nodes to the current node which haven't been expanded

    Args:
        grid_agent (tuple): It is the current environment
        curr_node (tuple): The current location of the grid agent 
        traversed_node (list): It is a closed list of nodes

    Returns:
        _type_: _description_
    """    
    curr_xnode, curr_ynode = curr_node
    imp_nodes = [(curr_xnode + 1, curr_ynode),
                (curr_xnode - 1, curr_ynode),
                (curr_xnode, curr_ynode+1),
                (curr_xnode, curr_ynode-1)]
    actualnodes = []
    for adj in imp_nodes:
        if grid_agent[adj] != 0 and adj not in traversed_node:
            actualnodes.append(adj)

  
    return actualnodes

def astar_plotting(grid_agent, g, source_node, exact_node, prev_node):
    """This  is used to plot the Astar path in the expanded cells

    Args:
        grid_agent (tuple): It is the current environment
        g (numpy array): The cost to go from source node to current node
        source_node (tuple): The node from which it start to traverse to the destination node
        exact_node (tuple): It is the current node
        prev_node (dictionary): Tree of nodes (basically we can backtrace it to the source node)
    """    
    temporary_gridagent = grid_agent.copy()
    n = exact_node
    while n != source_node:
        n = prev_node[n]
        temporary_gridagent[n] = 5

    temporary_gridagent[n] = 5

    img, (ax1, ax2) = plt.subplots(1,2, figsize = (30,10))
    img.suptitle('THIS IS THE PLOTTED A* PATH ', fontsize = 25, fontweight = 'bold')

    ax1.imshow(temporary_gridagent, cmap='jet', interpolation='none')
    ax2.imshow(g, cmap='jet', interpolation='none')

    ax1.set_title('GRID AGENT', fontsize= 15, fontweight='bold')
    ax2.set_title('REPRESENTING EXPANDED CELLS BY THE A* ALGORITHM',fontsize= 15, fontweight='bold')
    plt.show()


def astar_implementation(grid_agent, source_node, destination_node, h, g, f, g_traversed):
    """Here, we are implementing the astar algorithm

    Args:
        grid_agent (tuple): It is the current environment
        source_node (tuple): The node from which it start to traverse to the destination node
        destination_node (tuple): The node till where we need to trace the path
        h (numpy array): The h_score values 
        g (numpy array): The g_score values
        f (numpy array): The f_score values
        g_traversed (list): It is a closed list 

    Returns:
        dictionary : Dictionary for tracing back the path
    """    
    prev_node = {}
    traversed_node = []
    future_traversal = []

    path = False
    f[source_node] = h[source_node]
    g[source_node] = 0

    heappush(future_traversal, (f[source_node],h[source_node],source_node))
    while(future_traversal):
        _ , _1 , curr_node = heappop(future_traversal)
        f[curr_node] = g[curr_node] + h[curr_node]

        if h[curr_node] == 0:
            path = True

            g_traversed[destination_node] = g[destination_node]
            break

        next = adjacent(grid_agent, curr_node, traversed_node)

        for next_node in next:

            next_c = g[curr_node] + c
            open_set = [ pot_node for _,_,pot_node in future_traversal]
            if next_node in open_set:
                if g[next_node] <= next_c:
                    continue
                else:
                    g[next_node] = next_c
                    idx = future_traversal.index((f[next_node],h[next_node],next_node))
                    f[next_node] = g[next_node] + h[next_node]
                    future_traversal[idx] = (f[next_node], h[next_node], next_node)
                    heapify(future_traversal)
                    prev_node[next_node] = curr_node

            elif next_node in traversed_node:
                continue

            else:
                g[next_node] = next_c
                f[next_node] = g[next_node] + h[next_node]
                heappush(future_traversal , (f[next_node], h[next_node], next_node))
                prev_node[next_node] = curr_node

        traversed_node.append(curr_node)
        g_traversed[curr_node] = g[curr_node]

    if path == False:
        return False

    else:
        return prev_node
