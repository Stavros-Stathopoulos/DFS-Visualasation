import matplotlib.pyplot as plt
import networkx as nx

#The graph witch DFS is traversing
graph =  {
        'A': ['B','C'], 
        'B' : ['D', 'E'],
        'E' : ['H', 'I'], 
        'C' : ['J', 'K'], 
        'D' : ['F','G'], 
        'J' : ['L', 'M'], 
        'K' : ['N', 'O'], 
        'F' : [], 
        'G' : [], 
        'H' : [], 
        'I' : [],
        'L' : [], 
        'M' : [], 
        'N' : [], 
        'O' : []
        }

#2 lists that they are containing the results of the DFS traversal
visited = []
visited1 = []

#The main DFS function
def dfs (visited, graph, starting_node):
    if starting_node not in visited:
        print(starting_node, end=' ')
        visited.append(starting_node)
        for next in graph[starting_node]:
            dfs(visited, graph, next)
            if graph.keys()==visited:
                return(visited)

#Some colors so we dont hardcode them every time we use them
color_visited = "paleturquoise"
color_unvisited = "lightgrey"
color_current = "plum"
color_edge = "black"
bg_color = "white"

#Class Visualisation is responsible for creating the graph and the animations to visualize the DFS traversal
class Visualisation():
    #here are the coordinates so the graf nodes are in a specific order instead of random
    coordinates = {
            "A" : [8,8],
            "B" : [3,7],
            "C" : [13,7],
            "D" : [1,6],
            "E" : [5,6],
            "F" : [0,5],
            "G" : [3,5],
            "H" : [4,5],
            "I" : [7,5],
            "J" : [11,6],
            "K" : [15,6],
            "L" : [9,5],
            "M" : [12,5],
            "N" : [13,5],
            "O" : [17,5]
        }
    #The following list is demostraiting how the nodes are conecting
    node_connections = [
            ("A","B"),
            ("A", "C"), 
            ("B", "D"), 
            ("B", "E"), 
            ("D", "F"), 
            ("D", "G"), 
            ("E", "H"), 
            ("E", "I"),
            ("C","J"),
            ("C", "K"), 
            ("J", "L"), 
            ("J", "M"), 
            ("K", "N"), 
            ("K", "O") 
            
            ]

    def __init__(self):
        self.run()

    '''def graph is responisible to make a static diagram and some basic graphics.
        It is responsible to draw the unvisited graph and change colors'''
    def graph(self):
        
        plt.figure("DFS Algorithm Visualisation", figsize = (10,8))
        plt.suptitle("DFS Algorithm Visualisation", fontsize = 20)
        self.G = nx.DiGraph()
        self.G.add_edges_from(Visualisation.node_connections)

        self.pos = nx.spring_layout(self.G, k = 10, pos = Visualisation.coordinates, fixed = list(self.G.nodes()))

        nx.draw_networkx_nodes(self.G, self.pos, node_size = 350, node_color = color_unvisited)
        nx.draw_networkx_edges(self.G, self.pos, edgelist = self.G.edges(), edge_color = color_edge)
        nx.draw_networkx_labels(self.G, self.pos)
        plt.axis("off")
        self.steps()
        for i in range(len(list(self.dfs_steps))):
            self.frame(i)
        plt.show() 

    #def frame is animating the DFS traversal. It draws nodes with the right color if the node is visited or currently visited
    def frame(self, i):
        Graph = nx.DiGraph()
        Graph.add_edges_from(Visualisation.node_connections)
        pos = nx.spring_layout(self.G, k = 10, pos = Visualisation.coordinates, fixed = list(self.G.nodes()))
        text = "Currently in: " + self.step[i]
        plt.text(x=7, y=8.5, s=text, backgroundcolor = "white")        
        if self.step[i] not in visited1:
            visited1.append(self.step[i])
            text = "Visited sequence: " + str(visited1)
            plt.text(x=7, y=8.35, s=text, backgroundcolor = bg_color)
        nx.draw_networkx_nodes(self.step[i], pos, node_size = 400, node_color = color_current)   
        plt.pause(2)  
        nx.draw_networkx_nodes(self.step[i], pos, node_size = 400, node_color = color_visited)

    #def steps is describing the exact steps of the algorithn so frame can draw and saw them correct
    def steps(self):
        self.dfs_steps = list(nx.dfs_labeled_edges(self.G, source="A"))
        self.step = []
        for i in range(len(list(self.dfs_steps))):
            step = self.dfs_steps[i]
            if step[2] == "forward":
                self.step.append(step[1])
            else:
                self.step.append(step[0])   
    #def run is starting the whole program
    def run(self):
        print('Using DFS algorithm the nodes are visited in this order:')
        dfs(visited, graph, "A")
        self.graph()
        

if __name__ == "__main__":
   visited =[]
   Visualisation()