import pygame
import button
import math
import time
import heapq

# dictionary adjacency list

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

a = Point(0,0)
b = Point(5,0)
c = Point(3,6)
d = Point(7,6)
e = Point(13,4)
f = Point(4,16)
g = Point(9,12)
h = Point(14,17)

graph = {
    'A': {'B':b},
    'B': {'A':a, 'C':c, 'D':d, 'E':e},
    'C': {'B':b, 'F':f, 'G':g},
    'D': {'B':b, 'E':e},
    'E': {'B':b, 'D':d, 'G':g, 'H':h},
    'F': {'C':c, 'H':h},
    'G': {'C':c, 'E':e},
    'H': {'E':e, 'F':f}
}

graph2 = {
    'A': {'B':b},
    'B': {'A':a, 'D':d, 'E':e},
    'C': {'F':f, 'G':g},
    'D': {'B':b, 'E':e},
    'E': {'B':b, 'D':d, 'G':g},
    'F': {'C':c, 'H':h},
    'G': {'C':c, 'E':e},
    'H': {'F':f}
}

def dijkstra(graph, start, end):
    # Initialize distances and heap
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited_color = (0, 0, 0)
    label_color = (255, 0, 0)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, neighbor_point in graph[current_vertex].items():
            distance = current_distance + calculate_distance(graph, current_vertex, neighbor)
            
            if distance < distances[neighbor]:
                time.sleep(0.5)
                distances[neighbor] = distance
                rounded = round(distance, 2)
                draw_line(graph[current_vertex][neighbor], graph[neighbor][current_vertex], visited_color)
                label_line(graph[current_vertex][neighbor], graph[neighbor][current_vertex], str(rounded), label_color)
                pygame.display.update()
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[end]

def calculate_distance(graph, start, end):
    start_point = graph[start][end]
    end_point = graph[end][start]
    return ((start_point.x - end_point.x) ** 2 + (start_point.y - end_point.y) ** 2) ** 0.5

def draw_line(start, end, color):
    pygame.draw.line(screen, color, ((start.x * 20) + 20, (start.y * 20) + 20), ((end.x * 20) + 20, (end.y * 20) + 20), 5)

def label_line(start, end, label, color):
    midpoint = Point(round((start.x + end.x) / 2, 1), round((start.y + end.y) / 2, 1))
    text_surface = my_font.render(label, False, color)
    screen.blit(text_surface, ((midpoint.x * 20), (midpoint.y * 20) + 15))


def paint(graph, start, end):
    unvisited_color = (255, 255, 255)
    
    for i in graph:
        for j in graph[i]:
            draw_line(graph[i][j], graph[j][i], unvisited_color)
    
    for node in graph:
        for nestedNode in graph:
            if node != nestedNode and nestedNode in graph[node]:
                coords = ((graph[node][nestedNode].x * 20) + 20, (graph[node][nestedNode].y * 20) + 20)
                pygame.draw.circle(screen, (0,0,0), coords , 10)
                
    pygame.draw.circle(screen, (255,0,0), ((start.x * 20) + 20, (start.y * 20) + 20), 10)
    text_surface = my_font.render('START', False, (0, 0, 0))
    screen.blit(text_surface, ((start.x * 20), (start.y * 20) + 15))

    pygame.draw.circle(screen, (0,255,0), ((end.x * 20) + 20, (end.y * 20) + 20), 10)
    text_surface = my_font.render('END', False, (0, 0, 0))
    screen.blit(text_surface, ((end.x * 20) + 6, (end.y * 20) + 15))

resx = 1000
resy = 700
res = (resx, resy)

screen = pygame.display.set_mode(res)
pygame.display.set_caption('Graph')


#font stuff
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 20)
sol_font = pygame.font.SysFont('Comic Sans MS', 30)
screen.fill((92,161,104))
paint(graph, a, h)
start_vertex = "A"
end_vertex = "H"
result = dijkstra(graph, start_vertex, end_vertex)
text_surface = sol_font.render("The shortest distance with dijktras algorithm is " + str(round(result,1)), False, (0, 0, 0))
screen.blit(text_surface, (30, resy - 30))

print(f"Shortest distance from {start_vertex} to {end_vertex}: {result}")
#game loop
run = True
while run:
    #event handler
    for event in pygame.event.get():
        #quitgame
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
