import unittest
import pygame
from graph import dijkstra, Point

class TestDijkstraAlgorithm(unittest.TestCase):
    def setUp(self):
        self.a = Point(0,0)
        self.b = Point(1,1)
        self.c = Point(2,2)
        self.d = Point(2,1)
        self.e = Point(1,2)
        self.f = Point(5,5)
        self.g = Point(10,5)
        self.h = Point(5,10)
        self.i = Point(10,10)
        self.j = Point(0,1)
        self.k = Point(1,0)
        self.l = Point(0,2)
        self.m = Point(2,0)

        self.vA = 'A'
        self.vB = 'B'
        self.vC = 'C'
        self.vD = 'D'
        self.vE = 'E'
        self.vF = 'F'
        self.vD = 'G'
        self.vH = 'H'
        self.vI = 'I'

        

        self.dot = {
            'A': {}
        }

        self.line = {
            'A': {'B':self.b},
            'B': {'A':self.a}
        }

        self.chainOfShortOrOneLong = {
            'A': {'M': self.m, 'I': self.i},
            'M': {'A': self.a, 'D': self.d},
            'D': {'M': self.m, 'G': self.g},
            'G': {'D': self.d, 'I': self.i},
            'I': {'A': self.a, 'G': self.g}
        }

        self.cycles = {
            'A': {'J': self.j, 'K': self.k},
            'K': {'A': self.a, 'B': self.b, 'M': self.m},
            'J': {'A': self.a, 'B': self.b, 'I': self.i},
            'B': {'D': self.d, 'E': self.e, 'J': self.j, 'K': self.k},
            'I': {'E': self.e, 'J': self.j},
            'M': {'D': self.d, 'K': self.k},
            'D': {'B': self.b, 'C': self.c, 'M': self.m},
            'E': {'B': self.b, 'C': self.c, 'I': self.i},
            'C': {'D': self.d, 'E': self.e},
        }

        self.random = {
            'A': {'B':self.b},
            'B': {'A':self.a, 'C':self.c, 'D':self.d, 'E':self.e},
            'C': {'B':self.b, 'F':self.f, 'G':self.g},
            'D': {'B':self.b, 'E':self.e},
            'E': {'B':self.b, 'D':self.d, 'G':self.g, 'H':self.h},
            'F': {'C':self.c, 'H':self.h},
            'G': {'C':self.c, 'E':self.e},
            'H': {'E':self.e, 'F':self.f}
        }

    def test_dijkstra_dot(self):
        result = dijkstra(self.dot, 'A', 'A', self.a, self.a, True)
        self.assertAlmostEqual(result, 0, places=2)

    def test_dijkstra_line(self):
        result = dijkstra(self.line, 'A', 'B', self.a, self.b, True)
        self.assertAlmostEqual(result, 1.41, places=2)

    def test_dijkstra_chainOfShortOrOneLong(self):
        result = dijkstra(self.chainOfShortOrOneLong, 'A', 'I', self.a, self.b, True)
        self.assertAlmostEqual(result, 14.14, places=2)

    def test_dijkstra_cycles(self):
        result = dijkstra(self.cycles, 'A', 'C', self.a, self.c, True)
        self.assertAlmostEqual(result, 4.0, places=2)

    def test_dijkstra_random(self):
        result = dijkstra(self.random, 'A', 'H', self.a, self.h, True)
        self.assertAlmostEqual(result, 11.36, places=2)

if __name__ == '__main__':
    unittest.main()