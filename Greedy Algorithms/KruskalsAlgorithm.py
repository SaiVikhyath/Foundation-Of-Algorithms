# Author: Sai Vikhyath
# Date: 16 November, 2022


"""
Description:
"""


"""
Note:
"""


import cmath


class Kruskals:
    """
    """

    def __init__(self, numberOfVertices: int) -> None:
        """
        """
        
        self.numberOfVertices = numberOfVertices
        self.graph = [[0 for j in range(self.numberOfVertices)] for i in range(self.numberOfVertices)]

        for i in range(self.numberOfVertices):
            for j in range(self.numberOfVertices):
                if i >= j:
                    continue
                else:
                    self.graph[i][j] = self.graph[j][i] = float(input("Enter the distance between vertex " + str(i) + " and vertex " + str(j) + ": "))
        
    
    def kruskals(self) -> None:
        """
        """



if __name__ == "__main__":
    numberOfVertices = int(input("Enter the number of vertices: "))
    k = Kruskals(numberOfVertices)
    k.kruskals()