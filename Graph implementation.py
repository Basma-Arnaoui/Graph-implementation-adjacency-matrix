"""This is an implementation of a Graph, with two subclasses Vertex
and Edge with an adjacency matrix"""

class Graph:
 #--------NESTED VERTEX CLASS-------
    class Vertex:
        """each Vertex structure contains an element containing the
        information we want to stock"""

        __slots__ = "_element"

        def __init__(self, x):
            self._element = x

        def element(self):
            """Return the element contained in the Vertex"""
            return self._element

        def __hash__(self):
            return hash(id(self))

        def __eq__(self, other):
           return  self._element == other._element and type(self) == type(other)

 #------NESTED EDGE CLASS-----------

    class Edge:
        """Each Edge structure contains an the starting and
        ending vertex, and the element (weight of the edge)"""

        __slots__ = "_origin","_element","_destination"

        def __init__(self, u, v, x):

            self._origin = u
            self._element = x
            self._destination = v

        def endpoints(self):

            """Return (u,v) tuple for vertices u and v"""
            return (self._origin, self._destination)

        def opposite(self, u):
            """Return the vertex that is opposite to u"""
            return self._destination if u is self._origin else self._origin

        def element(self):
            """Return the element that is associated with the edge"""
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))

        def     __repr__(self):
            return "("+self._origin._element +   ","+ str(self._element)+ ","+ self._destination._element+")"


#-------REPRESENTATION OF A GRAPH USING AN ADJACENCY MATRIX----

    def __init__(self, directed = False):
        self._directed = directed
        self._matrix = [[]] #2D list with each element being an edge
        self._vertices = []
    def vertex_count(self):
        """Return the number of vertices in the graph"""
        return len(self._matrix)

    def vertices(self):
        """Return a list contaning all vertices"""
        return self._vertices

    def edge_count(self):
        """Return the number of edges, by counting how
        non None values in the matrix"""
        total = 0
        for i in range(len(self._matrix)):
            total += len(self._matrix[i])-self._matrix[i].count(None)
        return total if self._directed else total//2

    def edges(self):
        """Return a set containing all edges """
        result = []
        for i in self._matrix:
            for j in i:
                if j is not None:
                    result.append(j)
        return set(result) #avoid double values in undirected Graph

    def get_index(self, u):

        for i in range(len(self._vertices)):

            if self._vertices[i] == u:

               return i
        return None
             #Return the index of u and v in the vertices list
                            #so we can easily find them ine the matrix

    def get_edge(self, u, v):
        """Return the edge from u to v, or None if u and v are not adjacent"""

        indexes = (self.get_index(u), self.get_index(v))
        return self._matrix[indexes[0]][indexes[1]] if None not in indexes else None

            #will show None if indexes not found

    def degree(self, v, outgoing = True):
        """Return number of (outgoing) edges incident to vertex v
         in the graph (if G directed, optional parameter used to
         count incoming edges"""
        total = 0
        index = self.get_index(v)
        if outgoing:
            total = len(self._matrix[index])-self._matrix[index].count(None)
        else:
            for i in self._matrix:
                if i[index]!=None:
                    total += 1
        return total

    def incident_edges(self, v, outgoing = True):
        """Yield (outgoing) edges incident to vertex V
         in G. If graph is directed, optional parameter is
         used to request incoming edges"""
        index = self.get_index(v)
        for edge in self._matrix[index]:
            yield edge
    def insert_edge(self, u, v, x = None):
        """Insert and return a new Edge from u to v containing element x
        in an undirected graph ((u,v) == (v,u))"""
        e = self.Edge(u, v, x)
        u_index = self.get_index(u)

        v_index = self.get_index(v)
        self._matrix[u_index][v_index] = e
        self._matrix[v_index][u_index] = e

    def insert_vertex(self, x = None):
        """Insert and return a new vertex with element x"""
        v = self.Vertex(x)
        self._vertices.append(v)
        for row in self._matrix:
              row.append(None)

        self._matrix.append([None]*len(self._vertices))
        return v




