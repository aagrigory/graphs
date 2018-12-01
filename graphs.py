#!/usr/bin/env python
# coding: utf-8

def generate_edges(graph):
    edges = []
    for node in graph.keys():
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges

def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    isolated_nodes = []
    for node in graph.keys():
        if len(graph[node]) == 0:
            isolated_nodes.append(node)
    return isolated_nodes

class Graph(object):
    """ A simple Python graph class, demonstrating the essential facts and functionalities of graphs."""
    
    def __init__(self, graph_dict=None):
        """ Initializes a graph object. If no dictionary or None is given, an empty dictionary will be used"""
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        
    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())
    
    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()
    
    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict.keys():
            self.__graph_dict[vertex] = []        
        
    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; between two vertices can be multiple edges! """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict.keys():
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
            
    def __generate_edges(self):
        """ A static method generating the edges of the graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two vertices """
        edges = []
        for vertex in self.__graph_dict.keys():
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
#    def shortest_path(self, start, end, path=[]):
#        """ return the shortest path from the start node/vertex to end node/vertex"""
#        path += [start]
#        if start == end:
#            return path
#        if start not in self.__graph_dict.keys():
#            return None
#        for node in self.__graph_dict[start]:
#            newpath = self.shortest_path(self, self.__graph_dict, node, end, path=[])
#        return newpath
    
    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict.keys():
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
    
    def find_path(self, start_vertex, end_vertex, path=None):
        """find a path from start_vertex to end_vertex"""
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """find all paths from start_vertex to end_vertex"""
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_all_paths(vertex, end_vertex, path)
                
                for p in extended_path:
                    paths.append(p)
        return paths

    def find_shortest_path(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        graph = self.__graph_dict
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        
        shortest = None
        for node in graph[start_vertex]:
            if node not in path:
                newpath = self.find_shortest_path(node, end_vertex, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting
            it, i.e. the number of adjacent vertices. Loops are counted 
            double, i.e. every occurence of vertex in the list 
            of adjacent vertices. """ 
        if vertex not in self.__graph_dict:
            return None
        else:
            adjacent_vertices = self.__graph_dict[vertex]
            degree = len(adjacent_vertices) + adjacent_vertices.count(vertex)
            return degree
            
    def find_isolated_vertices(self):
        """ returns a list of isolated vertices. """
        isolated_vertices = []
        graph = self.__graph_dict
        for vertex in graph:
            if len(graph[vertex]) == 0:
                isolated_vertices.append(vertex)
        return isolated_vertices 
        
    def delta(self):
        """ the minimum degree of the vertices """
        min_degree = 10**10
        for vertex in self.__graph_dict:
            if self.vertex_degree(vertex) < min_degree:
                min_degree = self.vertex_degree(vertex)
        return min_degree
    
    def Delta(self):
        """ the maximum degree of the vertices """
        
        max_degree = 0
        for vertex in self.__graph_dict:
            if self.vertex_degree(vertex) > max_degree:
                max_degree = self.vertex_degree(vertex)
        return max_degree
    
    def degree_sequence(self):
        """ calculates the degree sequence """
        degree_sequence = []
        for vertex in self.__graph_dict:
            degree_sequence.append(self.vertex_degree(vertex))
        degree_sequence.sort(reverse=True)
        return degree_sequence
    
if __name__ == "__main__":
    g = { "a" : ["d", "g"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c", "g"],
          "e" : ["c"],
          "f" : [],
          "g" : ["a", "d"]
        }
    

    graph = Graph(g)
    ep = graph.find_path('a', 'e')
    print(ep)
    fal = graph.find_all_paths('a', 'e')
    print(fal)
    
    graph_shortest = graph.find_shortest_path('a', 'e')
    print(graph_shortest)    

