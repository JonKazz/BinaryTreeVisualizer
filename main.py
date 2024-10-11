import pygame
import sys
import collections
import math


SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
PADDING = 100
NODE_SIZE, NODE_WIDTH = 30, 4

nodes = [i for i in range(16)]
N = len(nodes)
HEIGHT = math.floor(math.log2(N)) + 1

# FORMULA FOR FINDING HEIGHTS
heights = [(2 * i - 1) / (2 * HEIGHT) * SCREEN_HEIGHT for i in range(1, HEIGHT + 1)]

# FORMULA FOR FINDING WIDTHS
widths = [((2 * i - 1) * SCREEN_WIDTH) / 2 ** HEIGHT for i in range(1, 2**(HEIGHT-1) + 1)] 

# BFS of array of nodes
q = collections.deque()
q.append(nodes[0])
node_coordinates = []

# Tracking each layer of binary tree
tree_level = 0 

while q:
    tree_level += 1
    
    # Using for drawing line between nodes
    previous_coordinate = set()
    
    # Height Coordinate (Calculated using 'heights' formula)
    hc = heights[tree_level-1]
    
    # Each width coordinates based on formula using tree level
    widths = [((2 * i - 1) * SCREEN_WIDTH) / 2 ** tree_level for i in range(1, 2**(tree_level-1) + 1)]
    
    for i in range(len(q)):
        node = q.popleft()
        
        # Width Coordinate
        wc = widths[i]
        
        # Adding coordinate to coordinate set
        node_coordinates.append((wc, hc))
        
        # Getting children of node and appending to queue
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        if left_child < N:
            q.append(left_child)
        if right_child < N:
            q.append(right_child)


pygame.init()
font = pygame.font.Font(None, 36)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Binary Tree Visualizer")

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    # BACKGROUND COLOR
    screen.fill((200, 220, 250))
                
    
    # Drawing the lines in between nodes. Must be drawn first so they are behind the nodes
    for idx in range(len(node_coordinates)):
        coordinate = node_coordinates[idx]
        parent_coordinate = node_coordinates[(idx - 1) // 2]
        
        if idx > 0:
            pygame.draw.line(screen, (0, 0, 0), parent_coordinate, coordinate, NODE_WIDTH)
        
        
    # Drawing each node    
    for idx in range(len(node_coordinates)):
        coordinate = node_coordinates[idx]
        parent_coordinate = node_coordinates[(idx - 1) // 2]
            
        pygame.draw.circle(screen, (255, 255, 255), coordinate, NODE_SIZE)
        pygame.draw.circle(screen, (0, 0, 0), coordinate, NODE_SIZE, NODE_WIDTH)
        text_surface = font.render(str(nodes[idx]), True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=coordinate)
        screen.blit(text_surface, text_rect)


    # Update the display
    pygame.display.flip()
pygame.quit()
