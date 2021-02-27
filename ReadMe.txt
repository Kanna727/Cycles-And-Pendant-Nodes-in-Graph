AUTHORS: 1506066 Prasanth Kanna 
        1506099 Sai Baba 
        1506090 Karthik Thakur 
        1506085 Hemanth Naik 
        1506100 Venkatesh Setti 
        1506048 Nishanth Shanmugam 

PREREQUESITES: Nothing needed. We have made this program to be completely STANDALONE and Can be run on any     PC by just installing it on that PC. Installing Pycharm or Python is optional 

PROGRAM DESCRIPTION: Developing a program that takes user given graph as an input & finds whether 
               there are any cycles or not, pendant vertex or not, and display them 

LANGUAGE USED: Python 3.6 (Included as a setup file in optional programs folder)

PLATFORM USED: PyCharm (Included as a setup file in optional programs folder)

TYPE OF GRAPH USED IN THE CODE: Directed Graph

NUMBER OF MODULES: 2: networkx & matplotlib 
 networkx: NetworkX is a Python package for the creation, manipulation, and  
                         study of the structure, dynamics, and functions of complex networks. 
	Features: 
	    1)Data structures for graphs, digraphs, and multigraphs 
	    2)Many standard graph algorithms 
	    3)Network structure and analysis measures 
	    4)Generators for classic graphs, random graphs, and synthetic networks 
	    5)Nodes can be "anything" (e.g., text, images, XML records) 
	    6)Edges can hold arbitrary data (e.g., weights, time-series) 
	    7)Open source 3-clause BSD license 
	    8)Well tested with over 1800 unit tests and >90% code coverage 
 matplotlib: Matplotlib is a Python 2D plotting library which produces publication quality figures  
             in a variety of hardcopy formats and interactive environments across platforms. 

INPUT FORMAT: Input line 1: Enter the nodes in a single line, separated by a single whitespace 
              Input line 2: Enter the number of edges(n) 
              Input lines n: Enter the starting node & ending node of each edge, separated by a single whitespace 

OUTPUT FORMAT: Output line 1: Prints number of cycles in the graph(n) 
               Output line 2: Prints list of nodes of each cycle 
               Output line 3: Prints number of pendant nodes in the graph 
               Output line 2: Prints list of pendant nodes 
               Graph 1: Displays main graph input by user 
               Graphs n: Displays all the cycles in the graph 1 
               Last Graph: Displays all the pendant nodes with their edges in a single graph 
               Representing Self-loops: Self-loops are represented by a * over the node's label 
               Representing Pendant Nodes: Pendant nodes are represented by their labels followed by (pen)  

INSTALLATION INSTRUCTIONS OF REQUIRED MODULES IN Pycharm FOR OUR SOURCE CODE: 
 1)Install Pycharm from the installer provided. Choose Python 3.6 during installation 
 2)Create a new empty project, named Graph, in pycharm. 
 3)Create a new python file in pycharm(alt+Enter) 
 4)Copy all the code from our source code to that file 
 5)Now we need to install the required modules to our project. To do that, open settings in pycharm(ctrl+alt+S) 
 6)Go to Project: Graph -> Project Interpretor 
 7)Click on the + sign near the right side margin of the window 
 8)Search for networkx and click on Install Package option at bottom 
 9)Repeat the same steps to install matplotlib package too. 
 10)To run the code press ctrl+F5
SOME CONCEPTS OF PYTHON WE USED IN OUR SOURCE CODE: 
1) List Comprehension:  List comprehensions provides a concise way to create lists.  
			It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists. The result will be a new list resulting from evaluating     the expression in the context of the for and if clauses which follow it.  
			The list comprehension always returns a result list.  
			If you used to do it like this: 
			     new_list = [] 
			     for i in old_list: 
			         if filter(i): 
			             new_list.append(expressions(i))  
		        You can obtain the same thing using list comprehension: 
				new_list = [expression(i) for i in old_list if filter(i)] 

SAVING THE OUTPUTS OF GRAPH TO AN IMAGE:
	1)For the every GUI window of each that generates, There will be a little save icon on that window
	2)Click on that window, and choose path, then the image of that graph will be saved.