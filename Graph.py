import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices = [], edges = []):
        self.vertices = vertices
        self.edges = edges
        self.x = [vertex[0] for vertex in vertices]
        self.y = [vertex[1] for vertex in vertices]
        print(self.vertices)
        
    def plot(self, padding = 1):
        fig, ax = plt.subplots()
        for vertex in self.vertices:
            ax.plot(vertex[0], vertex[1], 'o')
        for edge in self.edges:
            ax.plot([self.vertices[edge[0]][0], self.vertices[edge[1]][0]],
                    [self.vertices[edge[0]][1], self.vertices[edge[1]][1]], '-')
        plt.show()