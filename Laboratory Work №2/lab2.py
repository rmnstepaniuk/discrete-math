from tkinter import *
import random
from tkinter import messagebox

A = set()
B = set()
a = dict()
b = dict()
S = []
R = []
women_names = ["Olha", "Svitlana", "Julia", "Maryna", "Anastasia", "Anna", "Maria", "Olena"]
men_names = ["Victor", "Bohdan", "Igor", "Roman", "Ivan", "Anatoliy", "Pavlo", "Vladyslav"]

root = Tk()
root.title("Lab #2 | Window 1")
# root.geometry("1150x525")
root.config(bg = "#00FF99")

def wind_2():

    state = IntVar(0)
    
    def women_add(event):
        global A, B
        if (state.get() == 0):
            A.add(women_names[event.widget.curselection()[0]])
            A_txt.insert(INSERT, women_names[event.widget.curselection()[0]] + " ")
        if (state.get() == 1):
            B.add(women_names[event.widget.curselection()[0]])
            B_txt.insert(INSERT, women_names[event.widget.curselection()[0]] + " ")
        
    def men_add(event):
        global A, B
        if (state.get() == 0):
            A.add(men_names[event.widget.curselection()[0]])
            A_txt.insert(END, men_names[event.widget.curselection()[0]] + " ")
        if (state.get() == 1):
            B.add(men_names[event.widget.curselection()[0]])
            B_txt.insert(END, men_names[event.widget.curselection()[0]] + " ")

    def save():
        with open(r"A.txt", "w", encoding="utf-8") as w:
            w.write(str(A_txt.get(1.4, END)))
        with open(r"B.txt", "w", encoding="utf-8") as w:
            w.write(str(B_txt.get(1.4, END)))

    def clear():
        A_txt.delete(1.4, END)
        B_txt.delete(1.4, END)

    def show():
        show = Toplevel(wind_2)
        show.title("Window 2 | Sets")
        show.config(bg = "#00FF99")

        a_lbl = Label(show, bg = "#66CC33", padx = 10, pady = 5)
        b_lbl = Label(show, bg = "#66CC33", padx = 10, pady = 5)

        f = open(r"A.txt", "r")
        g = open(r"B.txt", "r")
        a = f.read()
        b = g.read()

        a_lbl["text"] = "A = {}".format(a)
        f.close()
        b_lbl["text"] = "B = {}".format(b)
        g.close()

        a_lbl.grid(row = 0, column = 0, padx = 10, pady = 10)
        b_lbl.grid(row = 1, column = 0, padx = 10, pady = 10)

    wind_2 = Toplevel(root)
    wind_2.title("Window 2")
    wind_2.config(bg = "#00FF99")
   
    # W O M E N
    women_fr = LabelFrame(wind_2, text = "Women Names", padx = 10, pady = 10, bg = "#66CC33")
    women_lstbox = Listbox(women_fr, width = 15)
    
    for i in women_names:
        women_lstbox.insert(END, i)
    women_lstbox.bind("<<ListboxSelect>>", women_add)

    women_lstbox.grid(row = 0, column = 0, padx = 10, pady = 5)
    women_fr.grid(row = 0, column = 0, padx = 10, pady = 10)

    # M E N
    men_fr = LabelFrame(wind_2, text = "Men Names", padx = 10, pady = 10, bg = "#66CC33")
    men_lstbox = Listbox(men_fr, width = 15)   
    
    for i in men_names:
        men_lstbox.insert(END, i)
    men_lstbox.bind("<<ListboxSelect>>", men_add)

    men_lstbox.grid(row = 0, column = 1, padx = 10, pady = 5)
    men_fr.grid(row = 0, column = 1, padx = 10, pady = 10)
    
    # R A D I O    B U T T O N S
    radb_women = Radiobutton(wind_2, text = "Set A", variable = state, value = 0, bg = "#009933")
    radb_men = Radiobutton(wind_2, text = "Set B",  variable = state, value = 1, bg = "#009933")
    radb_women.grid(row = 1, column = 0, padx = 10, pady = 5)
    radb_men.grid(row = 1, column = 1, padx = 10, pady = 5)

    # S E T S
    set_fr = LabelFrame(wind_2, text = "Sets A and B", padx = 10, pady = 10, bg = "#66CC33")

    A_txt = Text(set_fr, height = 1, width = 50)
    A_txt.insert(INSERT, "A = ")
    A_txt.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 5)

    B_txt = Text(set_fr, height = 1, width = 50)
    B_txt.insert(INSERT, "B = ")
    B_txt.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 5)

    set_fr.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10)

    # B U T T O N S

    save_b = Button(wind_2, text = "Save Sets", width = 20, padx = 10, pady = 5, bg = "#009933", command = save)
    save_b.grid(row = 3, column = 0, padx = 10, pady = 10)

    clear_b = Button(wind_2, text = "Clear Sets", width = 20, padx = 10, pady = 5, bg = "#009933", command = clear)
    clear_b.grid(row = 3, column = 1, padx = 10, pady = 10)

    show_b = Button(wind_2, text = "Show from File", width = 50, padx = 10, pady = 5, bg = "#009933", command = show)
    show_b.grid(row = 4, column = 0, columnspan = 2, padx = 10, pady = 10)

    # M E N U
    menu2 = Menu(wind_2)
    wind_2.config(menu = menu2)
    wind2menu = Menu(menu2)
    wind2menu.add_command(label = "Window 3", command = wind_3)
    wind2menu.add_command(label = "Window 4", command = wind_4)
    menu2.add_cascade(label = "Windows", menu = wind2menu)

def wind_3():

    global A, B, women_names, men_names, S, R
    
    wind_3 = Toplevel(root)
    wind_3.title("Window 3")
    wind_3.config(bg = "#00FF99")

    # S E T S
    A_fr = LabelFrame(wind_3, text = "Set A", padx = 10, pady = 10, bg = "#66CC33")
    a_lstbox = Listbox(A_fr, width = 15)
    for i in A:
        a_lstbox.insert(END, i)

    a_lstbox.grid(row = 0, column = 0, padx = 10, pady = 5)
    A_fr.grid(row = 0, column = 0, padx = 10, pady = 10)

    B_fr = LabelFrame(wind_3, text = "Set B", padx = 10, pady = 10, bg = "#66CC33")
    b_lstbox = Listbox(B_fr, width = 15)   
    for i in B:
        b_lstbox.insert(END, i)

    b_lstbox.grid(row = 0, column = 1, padx = 10, pady = 5)
    B_fr.grid(row = 1, column = 0, padx = 10, pady = 10)  

    # C H I L D ' S    G O D F A T H E R    (К У М)
    relS_fr = LabelFrame(wind_3, text = "Set aSb, if a is a child's godfather of b", bg = "#66CC33")
    canvasS = Canvas(relS_fr, width = 450, height = 100, bg = "#66CC33")

    A_S = dict()
    B_S = dict()
    for i in range(len(A)):
        canvasS.create_text(30 + i*50, 10, text = list(A)[i])
        canvasS.create_oval([30 + i*50, 20], [40 + i*50, 30], fill = "red")
        A_S.update({list(A)[i]: [35 + i*50, 30]})
    for i in range(len(B)):
        canvasS.create_text(30 + i*50, 90, text = list(B)[i])
        canvasS.create_oval([30 + i*50, 70], [40 + i*50, 80], fill = "blue")
        B_S.update({list(B)[i]: [35 + i*50, 70]})

    I = 0
    for i in A:
        if (i in men_names):
            J = 0
            for j in B:
                k = random.randint(0, 5)
                if k == 1:
                    canvasS.create_line(A_S.get(i), B_S.get(j), width = 2, arrow = LAST)
                    S.append([i, j])
                    J += 1
                else: J += 1
            I += 1
        elif ((i in women_names) or (i in B)): I += 1

    canvasS.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
    relS_fr.grid(row = 0, column = 1, columnspan = 2, padx = 10, pady = 10)

    # G O D F A T H E R    (Х Р Е Щ Е Н И Й    Б А Т Ь К О)
    relR_fr = LabelFrame(wind_3, text = "Set aRb, if a is a godfather of b", bg = "#66CC33")
    canvasR = Canvas(relR_fr, width = 450, height = 100, bg = "#66CC33")

    A_R = dict()
    B_R = dict()
    for i in range(len(A)):
        canvasR.create_text([30 + i*50, 10], text = list(A)[i])
        canvasR.create_oval([30 + i*50, 20], [40 + i*50, 30], fill = "red")
        A_R.update({list(A)[i]: [35 + i*50, 30]})
    for i in range(len(B)):
        canvasR.create_text(30 + i*50, 90, text = list(B)[i])
        canvasR.create_oval([30 + i*50, 70], [40 + i*50, 80], fill = "blue")
        B_R.update({list(B)[i]: [35 + i*50, 70]})

    I = 0
    for i in A:
        if (i in men_names):
            J = 0
            for j in B:
                k = random.randint(0, 5)
                if k == 1:
                    canvasR.create_line([35 + I*50, 30], [35 + J*50, 70], width = 2, arrow = LAST)
                    R.append([i, j])
                    J += 1
                else: J += 1
            I += 1
        elif ((i in women_names) or (i in B)): I += 1

    canvasR.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
    relR_fr.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 10)

    # M E N U
    menu3 = Menu(wind_3)
    wind_3.config(menu = menu3)
    wind3menu = Menu(menu3)
    wind3menu.add_command(label = "Window 2", command= wind_2)
    wind3menu.add_command(label = "Window 4", command= wind_4)
    menu3.add_cascade(label = "Windows", menu = wind3menu)

def wind_4():

    global S, R, a, b


    wind_4 = Toplevel(root)
    wind_4.title("Window 4")
    wind_4.config(bg = "#00FF99")

    def RunionS():
        
        global a, b

        U = R + S

        graph.delete("all")
        RuS.config(bg = "#009933")
        RiS.config(bg = "#FFFFFF")
        RdS.config(bg = "#FFFFFF")
        Rcomp.config(bg = "#FFFFFF")
        Strans.config(bg = "#FFFFFF")

        for i in range(len(A)):
            graph.create_text(30 + i*50, 10, text = list(A)[i])
            graph.create_oval([30 + i*50, 20], [40 + i*50, 30], fill = "red")
            a.update({list(A)[i]: [35 + i*50, 30]})
        for i in range(len(B)):
            graph.create_text(30 + i*50, 90, text = list(B)[i])
            graph.create_oval([30 + i*50, 70], [40 + i*50, 80], fill = "blue")
            b.update({list(B)[i]: [35 + i*50, 70]})
        for i in U:
            graph.create_line(a[i[0]], b[i[1]], width = 2, arrow = LAST)

    def RintersectionS():

        I = []
        for i in R:
            if i in S:
                I.append(i)

        graph.delete("all")
        RiS.config(bg = "#009933")
        RuS.config(bg = "#FFFFFF")
        RdS.config(bg = "#FFFFFF")
        Rcomp.config(bg = "#FFFFFF")
        Strans.config(bg = "#FFFFFF")

        for i in range(len(A)):
            graph.create_text(30 + i*50, 10, text = list(A)[i])
            graph.create_oval([30 + i*50, 20], [40 + i*50, 30], fill = "red")
        for i in range(len(B)):
            graph.create_text(30 + i*50, 90, text = list(B)[i])
            graph.create_oval([30 + i*50, 70], [40 + i*50, 80], fill = "blue")
        for i in I:
            if (len(I) != 0):
                graph.create_line(a[i[0]], b[i[1]], width = 2, arrow = LAST)
        

    def RdifferenceS():

        D = []
        for i in R:
            if (i not in S):
                D.append(i)

        graph.delete("all")
        RdS.config(bg = "#009933")
        RiS.config(bg = "#FFFFFF")
        RuS.config(bg = "#FFFFFF")
        Rcomp.config(bg = "#FFFFFF")
        Strans.config(bg = "#FFFFFF")

        for i in range(len(A)):
            graph.create_text(30 + i*50, 10, text = list(A)[i])
            graph.create_oval([30 + i*50, 20], [40 + i*50, 30], fill = "red")
        for i in range(len(B)):
            graph.create_text(30 + i*50, 90, text = list(B)[i])
            graph.create_oval([30 + i*50, 70], [40 + i*50, 80], fill = "blue")
        for i in D:
            graph.create_line(a[i[0]], b[i[1]], width = 2, arrow = LAST)

    def Rcomplement():

        C = []
        U = []
        for i in A:
            for j in B:
                U.append([i, j])
        for i in U:
            if (i not in R):
                C.append(i)

        graph.delete("all")
        Rcomp.config(bg = "#009933")
        RiS.config(bg = "#FFFFFF")
        RdS.config(bg = "#FFFFFF")
        RuS.config(bg = "#FFFFFF")
        Strans.config(bg = "#FFFFFF")

        for i in range(len(A)):
            graph.create_text(30 + i*50, 10, text = list(A)[i])
            graph.create_oval([30 + i*50, 20], [40 + i*50, 30], fill = "red")
        for i in range(len(B)):
            graph.create_text(30 + i*50, 90, text = list(B)[i])
            graph.create_oval([30 + i*50, 70], [40 + i*50, 80], fill = "blue")
        for i in C:
            graph.create_line(a[i[0]], b[i[1]], arrow = LAST)

    def Stransposition():

        graph.delete("all")
        Strans.config(bg = "#009933")
        RiS.config(bg = "#FFFFFF")
        RdS.config(bg = "#FFFFFF")
        Rcomp.config(bg = "#FFFFFF")
        RuS.config(bg = "#FFFFFF")

        for i in range(len(A)):
            graph.create_text(30 + i*50, 10, text = list(A)[i])
            graph.create_oval([30 + i*50, 20], [40 + i*50, 30], fill = "red")
        for i in range(len(B)):
            graph.create_text(30 + i*50, 90, text = list(B)[i])
            graph.create_oval([30 + i*50, 70], [40 + i*50, 80], fill = "blue")
        for i in S:
            graph.create_line(a[i[0]], b[i[1]], width = 2, arrow = FIRST)

    def clear():
        graph.delete("all")

    # B U T T O N S
    bttns_fr = LabelFrame(wind_4, bg = "#66CC33", padx = 10, pady = 5)

    RuS = Button(bttns_fr, text = "R ∪ S", command = RunionS, width = 10, padx = 10, pady = 5)
    RuS.grid(row = 0, column = 0, padx = 10, pady = 10)

    RiS = Button(bttns_fr, text = "R ∩ S", command = RintersectionS, width = 10, padx = 10, pady = 5)
    RiS.grid(row = 0, column = 1, padx = 10, pady = 10)

    RdS = Button(bttns_fr, text = "R \ S", command = RdifferenceS, width = 10, padx = 10, pady = 5)
    RdS.grid(row = 0, column = 2, padx = 10, pady = 10)

    Rcomp = Button(bttns_fr, text = "U \ R", command = Rcomplement, width = 10, padx = 10, pady = 5)
    Rcomp.grid(row = 0, column = 3, padx = 10, pady = 10)

    Strans = Button(bttns_fr, text = "S⁻¹", command = Stransposition, width = 10, padx = 10, pady = 5)
    Strans.grid(row = 0, column = 4, padx = 10, pady = 10)

    bttns_fr.grid(row = 0, column = 0, padx = 10, pady = 10)

    clear = Button(wind_4, text = "Clear Canvas", bg = "#009933", command = clear, padx = 10, pady = 5, width = 80)
    clear.grid(row = 2, column = 0, columnspan = 5, padx = 10, pady = 10)

    # G R A P H    C A N V A S
    canv_fr = LabelFrame(wind_4, width = 600, bg = "#66CC33", padx = 10, pady = 5)

    graph = Canvas(canv_fr, width = 450, height = 100, bg = "#66CC33")


    graph.grid(row = 0, column = 0, padx = 10, pady = 10)

    canv_fr.grid(row = 1, column = 0, columnspan = 5, padx = 10, pady = 10)

    # M E N U
    menu4 = Menu(wind_4)
    wind_4.config(menu = menu4)
    wind4menu = Menu(menu4)
    wind4menu.add_command(label = "Window 2", command= wind_2)
    wind4menu.add_command(label = "Window 3", command= wind_3)
    menu4.add_cascade(label = "Windows", menu = wind4menu)


### Info ####
def inf():
    info_fr.config(bg = "#66CC33")
    info_b.config(bg = "#009933")
    name = Label(info_fr, text = "Степанюк Р. В.", justify = 'left', pady = 2, bg = "#66CC33")
    group_n = Label(info_fr, text = "", justify = 'left', bg = "#66CC33")
    num = Label(info_fr, text = "", justify = 'left', pady = 2, bg = "#66CC33")
    var = Label(info_fr, text = "", justify = 'left', bg = "#66CC33")

    name.grid(row = 1, column = 0)
    group_n.grid(row = 2, column = 0)
    num.grid(row = 1, column = 1)
    var.grid(row = 2, column = 1)

    G = 91
    N = 25
    M = "ІВ"
    group_n["text"] = "My group: " + M + " - " + str(G)
    num["text"] = "My number: " + str(N)
    if M == "ІО": N += 2
    var["text"] = "My variant: " + str((N + G % 60) % 30 + 1)

info_fr = LabelFrame(root, text = "Student Info", padx = 15, pady = 15, bg = "#CC0000")
info_b = Button(info_fr, text = "Show info", width = 90, command = inf, bg = "#FF0000")

info_b.grid(row = 0, column = 0, columnspan = 2)
info_fr.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

#### Menu ####
menubar = Menu(root)
windowmenu = Menu(menubar, tearoff = 0)
root.config(menu = menubar)
windowmenu.add_separator()
windowmenu.add_command(label = "Window 2", command = wind_2)
windowmenu.add_command(label = "Window 3", command = wind_3)
windowmenu.add_command(label = "Window 4", command = wind_4)
menubar.add_cascade(label = "Windows", menu = windowmenu)

root.mainloop()