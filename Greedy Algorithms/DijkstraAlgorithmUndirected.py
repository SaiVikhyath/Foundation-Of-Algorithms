# Author: Sai Vikhyath
# Date: 16 November, 2022


"""
Description:
Given an undirected graph, G = (V, E) and a source vertex (S),
Find the shortest path from source to all other vertices.
"""


"""
Note:
Edges are considered as non-zero and non-negative.
No cycles and loops in the graph.
"""


import cmath


class Dijkstra:
    """
    Given an undirected graph, G = (V, E) and a source vertex (S),
    Starting from source, Compute the shortest path from source to the connected vertices,
    Repeat this until all the vertices are visted which by intuition gives the shortest path to all vertices from the source.
    """

    def __init__(self, numberOfVertices: int, source: int) -> None:
        """
        Maintain total number of vertices and the source vertex.
        Maintain the graph in a 2-D matrix where row and column index represents the vertices and the cells represent edge values.
        """
        
        self.numberOfVertices = numberOfVertices
        self.source = source
        self.graph = [[0 for j in range(self.numberOfVertices)] for i in range(self.numberOfVertices)]

        for i in range(self.numberOfVertices):
            for j in range(self.numberOfVertices):
                if i >= j:
                    continue
                else:
                    self.graph[i][j] = self.graph[j][i] = float(input("Enter the distance between vertex " + str(i) + " and vertex " + str(j) + ": "))
        
        

    def minimumDistanceVertex(self, distance, shortestPath) -> None:
        """ Compute the minimum distance vertex from all the unexplored vertices"""
        
        minimumIndex = cmath.inf
        minimumDistance = cmath.inf

        for i in range(self.numberOfVertices):
            if distance[i] < minimumDistance and shortestPath[i] == False:
                minimumIndex = i
                minimumDistance = distance[i]

        return minimumIndex


    def dijkstra(self) -> None:
        """
        Maintain a distance array containing the shortest distance to all the vertices from the source.
        Initialize the distance[source] to 0 and all the other distances to infinity.
        Maintain a set of unexplored nodes in shortestPath array.
        Assign False to all the vertices in shortestPath array indicating that at the start all vertices are unexplored.
        Then select the vertex with minimum distance among the unexplored vertices and update the weights of all the connected vertices.
        """

        distance = [cmath.inf] * self.numberOfVertices
        distance[self.source] = 0
        shortestPath = [False] * self.numberOfVertices

        for i in range(self.numberOfVertices):
            mv = self.minimumDistanceVertex(distance, shortestPath)
            shortestPath[mv] = True

            for v in range(self.numberOfVertices):
                if self.graph[mv][v] > 0 and shortestPath[v] == False and distance[v] > distance[mv] + self.graph[mv][v]:
                    distance[v] = distance[mv] + self.graph[mv][v]

        print("Distance of each vertex from source: ", distance)




if __name__ == "__main__":
    numberOfVertices = int(input("Enter the number of vertices: "))
    source = int(input("Enter the source vertex: "))
    d = Dijkstra(numberOfVertices, source)
    d.dijkstra()