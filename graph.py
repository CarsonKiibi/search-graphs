import pygame
import math
import time
import heapq

# dictionary adjacency list

# note pygame creates graphs as following:

#         *------------- +x ->
#         |
#         |
#         |
#         |
#         +y
#         |
#         \/

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

scaleFactor = 50    # how big the graph will be 
offset = 50         # offset from top left corner (0 would make )
increment = 0.5

visited_color = (0, 0, 0)
label_color = (255, 0, 0)


a = Point(0,0)
b = Point(1,1)
c = Point(2,2)
d = Point(2,1)
e = Point(1,2)
f = Point(5,5)
g = Point(10,5)
h = Point(5,10)
i = Point(10,10)
j = Point(0,1)
k = Point(1,0)
l = Point(0,2)
m = Point(2,0)

### add more graphs here

graph1 = {
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

cycles = {
            'A': {'J': j, 'K': k},
            'K': {'A': a, 'B': b, 'M': m},
            'J': {'A': a, 'B': b, 'L': l},
            'B': {'D': d, 'E': e, 'J': j, 'K': k},
            'L': {'E': e, 'J': j},
            'M': {'D': d, 'K': k},
            'D': {'B': b, 'C': c, 'M': m},
            'E': {'B': b, 'C': c, 'L': l},
            'C': {'D': d, 'E': e},
        }

# dijktras algorithm that also paints what has been searched 
def dijkstra(graph, start, end, startP, endP, test):
    paint(graph, startP, endP) if test == False else None

    # Initialize distances and heap
    try:
        if len(graph) == 0 or len(graph) == 1:
            return 0
        distances = {vertex: float('infinity') for vertex in graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, neighbor_point in graph[current_vertex].items():
                distance = current_distance + calculate_distance(graph, current_vertex, neighbor)
                
                if distance < distances[neighbor]:
                    time.sleep(increment) if test == False else None
                    distances[neighbor] = distance
                    rounded = round(distance, 2)

                    # draw over graph to show visited -> label will be total distance of that path so far
                    draw_line(graph[current_vertex][neighbor], graph[neighbor][current_vertex], visited_color) if test == False else None
                    label_line(graph[current_vertex][neighbor], graph[neighbor][current_vertex], str(rounded), label_color) if test == False else None

                    pygame.display.update() if test == False else None
                    heapq.heappush(priority_queue, (distance, neighbor))
        return distances[end]
    except: 
        print("graph invalid")
        return -1

#calculate distance from start to end of graph (for dijkstra)
def calculate_distance(graph, start, end):
    start_point = graph[start][end]
    end_point = graph[end][start]
    return ((start_point.x - end_point.x) ** 2 + (start_point.y - end_point.y) ** 2) ** 0.5

#draws line from start to end with color 
#-> given color parameter so we can draw the graph with this then overlay searched with new color
def draw_line(start, end, color):
    pygame.draw.line(screen, color, ((start.x * scaleFactor) + offset, (start.y * scaleFactor) + offset), ((end.x * scaleFactor) + offset, (end.y * scaleFactor) + offset), 5)

# finds middle of line and labels it
def label_line(start, end, label, color):
    midpoint = Point(round((start.x + end.x) / 2, 1), round((start.y + end.y) / 2, 1))
    text_surface = my_font.render(label, False, color)
    screen.blit(text_surface, ((midpoint.x * scaleFactor) + offset, (midpoint.y * scaleFactor) + offset))

# draws unsearched graph. dijkstras will draw over this
def paint(graph, start, end):
    unvisited_color = (255, 255, 255)
    
    for i in graph:
        for j in graph[i]:
            draw_line(graph[i][j], graph[j][i], unvisited_color)
    
    for node in graph:
        for nestedNode in graph:
            if node != nestedNode and nestedNode in graph[node]:
                coords = ((graph[node][nestedNode].x * scaleFactor) + offset, (graph[node][nestedNode].y * scaleFactor) + offset)
                pygame.draw.circle(screen, (0,0,0), coords , 10)
                
    pygame.draw.circle(screen, (0,255,0), ((start.x * scaleFactor) + offset, (start.y * scaleFactor) + offset), 10)
    text_surface = my_font.render('START', False, (0, 0, 0))
    screen.blit(text_surface, ((start.x * scaleFactor) + (offset / 2), (start.y * scaleFactor) + (offset / 2)))

    pygame.draw.circle(screen, (255,0,0), ((end.x * scaleFactor) + offset, (end.y * scaleFactor) + offset), 10)
    text_surface = my_font.render('END', False, (0, 0, 0))
    screen.blit(text_surface, ((end.x * scaleFactor) + (offset / 2), (end.y * scaleFactor) + (offset / 2)))

# create screen
resx = 1000
resy = 700
res = (resx, resy)

screen = pygame.display.set_mode(res)
pygame.display.set_caption('Graph')


#font stuff
pygame.font.init() # for module
my_font = pygame.font.SysFont('Comic Sans MS', 20)
sol_font = pygame.font.SysFont('Comic Sans MS', 30)
screen.fill((92,161,104))

#setup for dijkstra call
start_vertex = "A"
end_vertex = "C"
# start_vertex = startP
# -> eg "X" = x
startP = a
endP = c
result = dijkstra(cycles, start_vertex, end_vertex, startP, endP, False)

#pygame print result
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
