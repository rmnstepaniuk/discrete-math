from tkinter import *
import networkx as nx
from matplotlib import pyplot as plt

V = 9127 % 10 + 1 # варіант 8

def generate_graph(E):
    global G
    plt.clf()
    plt.figure(1)
    G = nx.gnp_random_graph(E, 0.3)
    nx.draw_circular(G, with_labels = 1)
    plt.show()

def create_path():
    global G

    def bfs_shortest_path(graph, start, goal):
        explored = []
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in explored:
                neighbours = graph[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == goal:
                        print("Пройдені вершини: " + str(new_path))
                        return new_path
                explored.append(node)

    path = bfs_shortest_path(G, int(path_node_1_entry.get()), int(path_node_2_entry.get()))

    path_edges = []

    for i in range(len(path)):
        try:
            path_edges.append([path[i], path[i+1]])
        except:
            IndexError
    print("Найкоротший шлях: " + str(path_edges))

    for i in G.edges():
        G[i[0]][i[1]]['color'] = 'black'
    for i in path_edges:
        G[i[0]][i[1]]['color'] = 'orange'

    coloring = [G[i[0]][i[1]]['color'] for i in G.edges()]

    plt.figure(2)
    nx.draw_circular(G, with_labels = True, edge_color = coloring)
    plt.show()

root = Tk()
root.title("Lab #3")
root.config(bg = "#00FF99")

# # # #   S T U D E N T    I N F O    # # # #

info_fr = LabelFrame(root, text = "S T U D E N T  I N F O", padx = 15, pady = 15, bg = "#66CC33")

name = Label(info_fr, text = "Степанюк Р. В.", justify = 'left', padx = 10, pady = 5, bg = "#66CC33")
group_n = Label(info_fr, text = "ІВ - 91", justify = 'left', padx = 10, pady = 5, bg = "#66CC33")
num = Label(info_fr, text = "НЗК: №9127", justify = 'left', padx = 10, pady = 5, bg = "#66CC33")
var = Label(info_fr, justify = 'left', padx = 10, pady = 5, bg = "#66CC33")

var["text"] = "Варіант " + str(V)

name.grid(row = 1, column = 0)
group_n.grid(row = 2, column = 0)
num.grid(row = 1, column = 1)
var.grid(row = 2, column = 1)

info_fr.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

# # # #  D A T A    I N P U T    # # # #

data_label = LabelFrame(root, text = "D A T A  I N P U T", bg = "#66CC33", padx = 15, pady = 15)

node_frame = LabelFrame(data_label, text = "Enter number of nodes", bg = "#66CC33")

node_entry = Entry(node_frame, width = 24, relief = SUNKEN)
node_entry.grid(row = 1, column = 0, padx = 10, pady = 10)

node_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

path_frame = LabelFrame(data_label, text = "Enter nodes that create path", bg = "#66CC33")

path_node_1_entry = Entry(path_frame, width = 15, relief = SUNKEN)
path_node_2_entry = Entry(path_frame, width = 15, relief = SUNKEN)

path_node_1_entry.grid(row = 1, column = 1, padx = 1, pady = 10)
path_node_2_entry.grid(row = 1, column = 2, padx = 1, pady = 10)

path_frame.grid(row = 0, column = 1, padx = 10, pady = 10)

data_label.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)

graph_B = Button(root, text = "Generate graph", command = lambda: generate_graph(int(node_entry.get())), width = 20, bg = "#009933", padx = 5, pady = 5)
graph_B.grid(row = 2, column = 0, padx = 10, pady = 10)

path_B = Button(root, text = "Find path", command = create_path, width = 20, bg = "#009933", padx = 5, pady = 5)
path_B.grid(row = 2, column = 1, padx = 10, pady = 10)

root.mainloop()