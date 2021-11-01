from tkinter import *
import networkx as nx
from matplotlib import pyplot as plt
from random import randint

colors = ['red', 'blue', 'green', 'yellow', 'olive', 'black', 'lime', 'purple', 'cyan', 'grey', 'maroon']
V = 9127 % 6 + 1 # варіант 2

def matrix_settings(n):
    global entries, matrix

    def on_click(event):
        if event.widget.get() == "0":
            event.widget.delete(0, END)
            event.widget.insert(END, "1")
        else:
            event.widget.delete(0, END)
            event.widget.insert(END, "0")

    def set_matrix():
        global matrix
        matrix = [] 
        for row in entries:
            matrix.append([])
            for entry in row:
                matrix[entries.index(row)].append(int(entry.get()))

    def random_matrix():
        for row in entries:
            for entry in entries:
                entries[entries.index(row)][entries.index(entry)].delete(0, END)
                entries[entries.index(row)][entries.index(entry)].insert(END, randint(0, 1))

    matrix_window = Toplevel(root)
    matrix_window.title("Lab #4 | Matrix")
    matrix_window.config(bg = "#00FF99")

    matrix_frame = LabelFrame(matrix_window, padx = 15, pady = 15, bg = "#66CC33")

    for i in range(n):
        l = Label(matrix_frame, bg = "#009933", text = i + 1)
        l.grid(row = 0, column = i + 1)
    for i in range(n):
        l = Label(matrix_frame, bg = "#009933", text = i + 1)
        l.grid(row = i + 1, column = 0, sticky = E)

    entries = []
    for r in range(n):
        entries.append([])
        for c in range(n):
            entry = Entry(matrix_frame, bg = "#66CC33", width = 3, justify = CENTER)
            entry.grid(row = r + 1, column = c + 1)
            entry.insert(END, "0")
            entry.bind('<Button-1>', on_click)
            entries[r].append(entry)

    matrix_frame.grid(row = 0, column = 0, padx = 15, pady = 15)

    button_frame = LabelFrame(matrix_window, text = "M A T R I X    S E T T I N G S", padx = 15, pady = 15, bg = "#66CC33")

    set_matrix_B = Button(button_frame, text = "Set Matrix", bg = "#009933", command = set_matrix, padx = 5, pady = 5)
    set_matrix_B.grid(row = 0, column = 0, padx = 5, pady = 5)

    random_matrix_B = Button(button_frame, text = "Random Matrix", bg = "#009933", command = random_matrix, padx = 5, pady = 5)
    random_matrix_B.grid(row = 0, column = n - 1, padx = 5, pady = 5)

    button_frame.grid(row = 1, column = 0, columnspan = n, padx = 5, pady = 5)

def generate_graph(E):
    global G, matrix
    plt.clf()
    plt.figure(1)

    for i in range(E):
        for j in range(E):
            if i == j:
                matrix[i][j] = 0
            elif i > j:
                matrix[i][j] = matrix[j][i]

    print("Symmertic matrix:")
    for i in matrix:
        print(i)

    G = nx.Graph()
    for i in range(E):
        G.add_node(i)
    for i in range(E):
        for j in range(E):
            if matrix[i][j] == 1:
                G.add_edge(i, j)
                
    nx.draw_circular(G, with_labels = 1)
    plt.show()

def color_graph():
    global colors

    n = int(node_entry.get())

    def getkey(item):
        return item[1]

    node_degree = []
    for node in G.nodes():
        node_degree.append([node, G.degree(node)])
    
    node_degree.sort(key = getkey, reverse = True)

    def coloring():

        def colorcheck(node, color): 
            p = True
            for i in list(G[node]):
                if ((matrix[i][int(node)] == 1) and (node_color.get(i, NONE) == colors[color])):
                    p = False
            return p 

        curcolor = 0
        painted = []
        node_color = {}
        for node, degree in node_degree:
            neighbours_node = list(G[node])
            if node not in painted:
                node_color.update({node: colors[curcolor]})
                painted.append(node)
            for i in G.nodes():
                if (i not in neighbours_node):
                    if (i not in painted):
                        if (colorcheck(i, curcolor) == True):
                            node_color.update({i: colors[curcolor]})
                            painted.append(i)
                else: pass
            curcolor += 1
        return node_color

    coloring = coloring()
    
    node_colormap = []
    for i in range(n):
        node_colormap.append(coloring[i])

    plt.figure(2)
    nx.draw_circular(G, with_labels = 1, node_color = node_colormap) 
    plt.show()

root = Tk()
root.title("Lab #4")
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

# # # #   D A T A  I N P U T   # # # #

data_label = LabelFrame(root, text = "D A T A  I N P U T", bg = "#66CC33", padx = 15, pady = 15)

node_frame = LabelFrame(data_label, text = "Enter number of nodes", bg = "#66CC33")

node_entry = Entry(node_frame, width = 24, relief = SUNKEN)
node_entry.grid(row = 1, column = 0, padx = 10, pady = 10)

node_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

data_label.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10)

graph_B = Button(root, text = "Generate graph", command = lambda: generate_graph(int(node_entry.get())), width = 20, bg = "#009933", padx = 5, pady = 5)
graph_B.grid(row = 2, column = 0, padx = 10, pady = 10)

coloring_B = Button(root, text = "Color the graph", command = color_graph, width = 20, bg = "#009933", padx = 5, pady = 5)
coloring_B.grid(row = 2, column = 1, padx = 10, pady = 10)

matrix_B = Button(root, text = "Matrix settings", command = lambda: matrix_settings(int(node_entry.get())), width = 50, bg = "#009933", padx = 5, pady = 5)
matrix_B.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10)

root.mainloop()