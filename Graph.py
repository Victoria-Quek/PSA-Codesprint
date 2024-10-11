import random

class Graph:
    # class constructor
    def __init__(self):
        self.vertices = []
    
    # checks whether the graph is empty
    def isEmpty(self):
        return len(self.vertices) == 0		
    
    def addVertex(self, vertex, x = None, y = None):
        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)
        if vertex in self.vertices:
            #print("Vertex already added in the graph!")
            return False
        if x == None or y == None:
            x = random.randrange(551)
            y = random.randrange(551)
        while self.isCoordsOccupied(x, y):
            x = random.randrange(551)
            y = random.randrange(551)
        self.vertices.append(vertex)
        if vertex.x == None:
            vertex.setCoords(x, y)
        return self.vertices
        
    def isCoordsOccupied(self, x, y):
        for v in self.vertices:
            coords = v.getCoords()
            if coords[0] >= x - 40 and coords[0] <= x + 40 and coords[1] >= y - 40 and coords[1] <= y + 40:
                return True
        return False
   
    
    def addEdge(self, v1, v2, weight = 1):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        for a in v1.adjList:
            if a[0] == v2:
                raise Exception('Edge already created!')
        v1._addEdge(v2, weight)
        
    def isAdj(self, v1, v2):
        for a in v1.adjList:
            if a[0] == v2:
                return True
        return False
    
    def deleteEdge(self, v1, v2):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if not self.isAdj(v1, v2):
            raise Exception('Vertex ' + str(v1.value) + ' does not have ' + str(v2.value) + ' edge')
        v1._deleteEdge(v2)
    
            
    #to count number of vertices in the graph
    def count_v(self):
        return len(self.vertices)
    
    #to delete the vertex from the graph        
    def deleteVertex(self, vertex):
        if not isinstance(vertex, Vertex):
            raise TypeError('value must be a Vertex!')
        if not vertex in self.vertices:
            raise ValueError('Vertex does not exist in graph')
        for e in self.vertices:
            e._deleteEdge(vertex)
        self.vertices.remove(vertex)
        return self.vertices
    
    # returns a string representation of the array
    def __repr__(self):	
        return str(self.vertices)
      
            
    def getVertexWithValue(self, value):
        for v in self.vertices:
            if v.value == value:
                return v

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

def shortest_path(graph, initial, target):
    visited = {initial: 0}
    paths = {}
    nodes = set(graph.vertices)
    while len(nodes) > 0:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node == None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]
        for node in min_node.adjList:
            weight = current_weight + node[1]
            if node[0] not in visited or weight < visited[node[0]]:
                visited[node[0]] = weight
                paths[node[0]] = min_node
    path = [target]
    next = target
    while next != initial:
        next = paths[next]
        path.append(next)
    return visited[target], path[::-1]