# Pygame Visual Graph Search (with Dijkstra's)
This pygame app will display a weighted, undirected graph and visually search it so the algorithm is easier to understand. It also outputs the value of the shortest path.
Algorithm info: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

## Setup

Make sure python 3 is installed.
```
pip install -r requirements.text
```
or simply 
```
pip install pygame==2.5.2
```

## Run the project
```
python3 graph.py
```

## Why this project 
I built this because I had not found anything like it. It has a lot of potential, whether it be easy things like adding new search algorithms or more difficult ones like letting the user draw there own graph.
During the summer or maybe even reading break of university I may implement this idea in javascript because it would be more accessible and pygame graphics aren't the best.

Feel free to modify this or create something based off it, and consider telling me about it on linkedin (www.linkedin.com/in/carson-kyba-51b0122a5). One big reason I created this was because the grid/pixel one seems so overdone now 
so I thought a weighted graph would be more interesting. Graphs are also a very interesting data structure that has a lot of unique applcations.

## Why represent the graph this way
The graph is represented as a adjacency list using a doubly nested dictionary (key-value pair). This makes looking up nodes fairly simple, and drawing the graph much easier. Also from the perspective of someone who may not be too familiar with graphs,
I feel this representation is much more intuitive then an adjacency matrix. It is still a pain to create a new graph, but I'm sure that's why I can't find a program where I can simply input a graph and visually search it.

I have never seen another project like this so that made picking the data structure a unique experience that I couldn't find a reference to. If anyone finds a project with the same functionality, let me know as I'd be interested to see it.
