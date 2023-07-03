# HERE, WE WILL START BY IMPORTING LIBRARIES 

import numpy as np
import matplotlib.pyplot as plt

def trajectory(prev_node, source_node, destination_node):
    prev_route = destination_node
    path = []
    while prev_route != source_node:
        path.append(prev_route)
        prev_route = prev_node[prev_route]
        
    path.reverse()
    return path

def show_route(showing_nodes, setup, grid_agent):
    show_route_xcoord, show_route_ycoord = showing_nodes
    show_adjacent = ((show_route_xcoord + 1, show_route_ycoord),
                        (show_route_xcoord - 1, show_route_ycoord),
                        (show_route_xcoord, show_route_ycoord + 1),
                        (show_route_xcoord, show_route_ycoord - 1))

    for adjacent in show_adjacent:
        grid_agent[adjacent] = setup[adjacent]

def show_trajectory(grid_agent, curr_node, counter, mode, setup, h, g_traversed, path):
    # Change "temporary_agent" & setup_temporary
    temporary_agent = grid_agent.copy()
    setup_temporary = setup.copy()

    for node in path:
        temporary_agent[node] = 3.5

    temporary_agent[curr_node] = 5
    setup_temporary[curr_node] = 5

    if mode == 'REPEATED FORWARD A*':
        plt.figure(figsize = (20,20))
        fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(30,10))
        fig.suptitle(f'Agent step {counter}',fontsize= 15, fontweight='bold')
        ax1.imshow(temporary_agent, cmap='jet', interpolation='none')
        ax2.imshow(setup_temporary, cmap='jet', interpolation='none')
        ax1.set_title('Agent Maze(Knowledge about the real maze as per agent)', fontsize= 15, fontweight='bold')
        ax2.set_title('Real Maze',fontsize= 15, fontweight='bold')

    elif mode == 'ADAPTIVE A*':
        plt.figure(figsize = (20,20))
        fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4,figsize=(30,10))
        fig.suptitle(f'Agent step {counter}',fontsize= 15, fontweight='bold')
        ax1.imshow(temporary_agent, cmap='jet', interpolation='none')
        ax2.imshow(setup_temporary, cmap='jet', interpolation='none')
        im3 = ax3.imshow(h, cmap='jet', interpolation='none')
        plt.colorbar(im3)
        ax3.imshow(h, cmap='jet', interpolation='none')
        ax4.imshow(g_traversed)
        ax1.set_title('Agent Maze(Knowledge about the real maze as per agent)', fontsize= 15, fontweight='bold')
        ax2.set_title('Real Maze',fontsize= 15, fontweight='bold')
        ax3.set_title('H values',fontsize= 15, fontweight='bold')
        ax4.set_title('Closed list generated for this particular iteration',fontsize= 15, fontweight='bold')

    plt.show()
     