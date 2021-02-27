import networkx as nx  # Imports networkx package for implementation of graphs
import matplotlib.pyplot as plt  # Imports matplotlib package for plotting and displaying the graphs

node=[]
edge=[]


# Return a list of nodes of each cycle
def cycles(G):
    l = list(nx.simple_cycles(G))
    if len(l) != 0:
        print('No. of cycles in the graph are: ', len(l), '\n')
        print('The nodes of each cycle are: ', l, '\n')
    else:
        print('There are no cycles in the given graph\n')
    return l


# Returns a list of edges incoming or outgoing via a pendant node
def pendant(G):
    deg = G.degree()  # creates a dictionary of degree of each node as value & label of each node as key
    e = []
    min_value = min(deg.values())  # finds the least degree
    if min_value == 1:  # if the least degree is 1
        min_keys = [k for k in deg if deg[k] == min_value]  # finds all the nodes with the degree 1 i.e., pendant nodes
        print('No. of pendant nodes are: ', len(min_keys), '\n')
        print('The pendant nodes are: ', min_keys, '\n')
        e = G.edges(min_keys)+G.in_edges(min_keys)  # creates a list of edges incoming or outgoing to or from a pendant node
        for i in range(0,len(e)):
            e[i]=list(e[i])
            for j in range(0,len(e[i])):
                if e[i][j] in min_keys:
                    e[i][j]=e[i][j]+'(pen)'
    else:
        print('There are no pendant nodes in the given graph\n')
    return e


# Draws a graph G
def draw(G,pos,name):

    nx.draw_networkx(G,pos=pos,with_labels=True, node_size = 200, node_color='orange',font_size=10)
    plt.axis('off')  # Will not display axes
    plt.title(name)  # Will display name on the graph
    plt.show()  # Displays the drawn graph


# Draws cycles in a graph
def draw_cycles(l, pos, name):
    if len(l)==0:
        X=nx.DiGraph()
        draw(X,pos,'No cycles are present the given graph')
    elif len(l)==1 and len(l[0])==1:
        X=nx.DiGraph()
        X.add_edge(l[0][0],l[0][0])
        nx.draw_networkx(X,pos=pos,with_labels=True, node_size = 200, node_color='orange',font_size=10)
        plt.axis('off')
        plt.title(name)
        plt.show()
    else:
        for i in range(0, len(l)):  # Traverses through each cycle
            X = nx.DiGraph()
            j = 0
            for j in range(0, len(l[i])-1):  # Traverses through nodes of each cycle
                X.add_node(l[i][j])  # Adds each node to the cycle graph
                X.add_edge(l[i][j], l[i][j+1])  # Adds each edge to the cycle graph except the last edge
            X.add_edge(l[i][j+1], l[i][0])  # Adds the last edge to the cycle graph
            nx.draw_networkx(X,pos=pos,with_labels=True, node_size = 200, node_color='orange',font_size=10)
            plt.axis('off')
            plt.title(name)
            plt.show()  # Draws each cycle as a graph

# Creates Directed Graph
G = nx.DiGraph()  # Graph that will contain Main Graph input by user
G_pend = nx.DiGraph()  # Graph that will contain pendant odes

if __name__ == "__main__":
    # Inputs details of graph from user
    print('Enter labels of nodes: (NOTE: Enter the nodes in a single line, separated by a single whitespace)\n')
    node = [x for x in input().split()]  # Lambda Expression to convert the input string(with each label separated by a space) & splits them & stores all the labels in a list
    print('Enter number of edges:\n')
    noe = int(input())
    print("Enter each edge: (NOTE: Enter the starting node & ending node of each edge, separated by a single whitespace)\n")
    for i in range(0, noe):
        y = []
        y = [x for x in input().split()]
        for i in range(0,2):  # Checks whether if user is giving valid edges or not
            if y[i] in node:
                continue
            else:
                print('Please enter edges between the entered nodes only. Try again!!!')
                exit()
        if y[0]==y[1]:  # if there is a self loop on a node, then it is represented in the graph as [node]*
            for i in range(0,len(node)):
                if node[i]==y[0]:
                    node[i]=y[0]+'*'
                    y[0]=y[1]=node[i]
            edge.append(y)  # Append each edge nodes to edge list
    G.add_nodes_from(node)  # Adds nodes list to the main graph
    G.add_edges_from(edge)  # Adds edges list to the main graph
    pos = nx.circular_layout(G)  # Fixes the positions of nodes in circular format
    list_cycles = cycles(G)  # Call function to find the list of nodes of each cycle in the main graph
    list_pend = pendant(G)  # Call function to find the list of edges of pendant nodes in the main graph
    G_pend.add_edges_from(list_pend)  # Adds edges of pendant nodes to the graph that displays pendant nodes
    pos1 = nx.circular_layout(G_pend)
    draw(G,pos,'Main Graph')  # Draws the main graph
    draw_cycles(list_cycles,pos,'Cycles')  # Draws each cycle of main graph, if any. I no cycles are there, the graph will be just an empty graph
    if len(list_pend)!=0:
        draw(G_pend,pos1,'Pendant nodes')  # Displays pendant nodes of main graph, if any. I no pendant nodes are there, the graph will be just an empty graph
    else:
        draw(G_pend,pos1,'There are no pendant nodes in the given graph')






