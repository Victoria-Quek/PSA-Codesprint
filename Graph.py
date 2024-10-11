class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__()
        
    def addEdge(self, v1, v2, weight = 1):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        for a in v1.adjList:
            if a[0] == v2:
                raise Exception('Edge already created!')
        v1._addEdge(v2, weight)
        v2._addEdge(v1, weight)
        
    def deleteEdge(self, v1, v2):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if not self.isAdj(v1, v2):
            raise Exception('Vertex ' + str(v1.value) + ' does not have ' + str(v2.value) + ' edge')
        v1._deleteEdge(v2)
        v2._deleteEdge(v1)
        
class TSPGraph(UndirectedGraph):
    def __init__(self):
        super().__init__()
        
    def addVertex(self, v, x, y):
        v.setCoords(x, y)
        if len(self.vertices) > 0:
            for u in self.vertices:
                self.addEdge(u, v)
        self.vertices.append(v)
    
    def addEdge(self, v1, v2):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        for a in v1.adjList:
            if a[0] == v2:
                raise Exception('Edge already created!')
        v1Coords = v1.getCoords()
        v2Coords = v2.getCoords()
        weight = ((v1Coords[0] - v2Coords[0]) ** 2 + (v1Coords[1] - v2Coords[1]) ** 2) ** 0.5
        v1._addEdge(v2, weight)
        v2._addEdge(v1, weight)
        
    def generateRandomNodes(self, num):
        for i in range(num):
            self.addVertex(i)
        for i in range(len(self.vertices) - 1):
            v1 = self.vertices[i]
            for j in range(i + 1, len(self.vertices)):
                v2 = self.vertices[j]
                self.addEdge(v1, v2)

class Vertex:
    
    def __init__(self, value, x = None, y = None):
        self.value = value 
        self.adjList = []
        self.setCoords(x, y)
		
    def getAdjList(self):
        return self.adjList

    #to add edge to this vertex
    def _addEdge(self, vertex, weight):
        if not isinstance(vertex, Vertex):
            raise TypeError("Value must be a Vertex!")
        if vertex == self:
            raise Exception("cannot add edge to itself")
        for a in self.adjList:
            if a[0] == vertex:
                raise Exception('Edge already exists')
        self.adjList.append([vertex, weight])
    
    def _deleteEdge(self, vertex):
        if not isinstance(vertex, Vertex):
            raise TypeError("Value must be a Vertex!")
        for i in range(len(self.adjList) - 1, -1, -1):
            if self.adjList[i][0] == vertex:
                self.adjList.pop(i)
    
    # return a string representation of the vertex
    def __repr__(self):
        return str(self.value)		
        
    def setCoords(self, x, y):
        self.x = x
        self.y = y
        
    def getCoords(self):
        return (self.x, self.y)
        
    def __eq__(self, other):
        return isinstance(other, Vertex) and self.value == other.value
        
    def __hash__(self):
        return hash(str(self.value))

    