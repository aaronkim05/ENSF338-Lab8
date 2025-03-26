class GraphNode:
    def __init__(self, data):
        self.data = data
        
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addNode(self, data):
        if data not in self.adjacency_list:
            node = GraphNode(data)
            self.adjacency_list[data] = {}
            return node
        return None

    def removeNode(self, node):
        if node.data in self.adjacency_list:
            del self.adjacency_list[node.data]
            for neighbors in self.adjacency_list.values():
                neighbors.pop(node.data, None)

    def addEdge(self, n1, n2, weight=1):
        if n1 in self.adjacency_list and n2 in self.adjacency_list:
            self.adjacency_list[n1][n2] = weight
            self.adjacency_list[n2][n1] = weight

    def removeEdge(self, n1, n2):
        if n1 in self.adjacency_list and n2 in self.adjacency_list[n1]:
            del self.adjacency_list[n1][n2]
            del self.adjacency_list[n2][n1]
