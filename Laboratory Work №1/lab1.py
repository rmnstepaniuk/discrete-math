from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Lab #1")
root.geometry("1150x525")
root.config(bg = "#00FF99")

A = set()
B = set()
C = set()
D = set()
U = set()
Z = set()
k = 0
l = 0
card_A = 0
card_B = 0
card_C = 0

#### Window 2 ####
def wind_2():

    global A
    global B
    global C
    global k
    s1 = set(A & B)
    s2 = set(C & B)
    s3 = set((U - A) & (U - B))
    s4 = set((U - B) & C)
    s5 = set(s1 | s2)
    s6 = set(s3 | s4)
    s7 = set(s5 | s6)

    def save():
        with open(r"D1.txt", "w", encoding="utf-8") as w:
            w.write(str(step_txt.get(2.7, END)))
    
    def step():
        global k
      
        #### Step 1 ####
        if (k == 0): 
            step_txt.delete(1.0, END)
            step_txt.insert(INSERT, "Operation : (A ∩ B)\nResult:" + str(s1))
            k += 1
        #### Step 2 ####
        elif (k == 1): 
            step_txt.delete(1.0, END)
            step_txt.insert(INSERT, "Operation : (C ∩ B)\nResult:" + str(s2))
            k += 1
        #### Step 3 ####
        elif (k == 2): 
            step_txt.delete(1.0, END)
            step_txt.insert(INSERT, "Operation : (¬A ∩ ¬B)\nResult:" + str(s3))
            k += 1
        #### Step 4 ####
        elif (k == 3): 
            step_txt.delete(1.0, END)
            step_txt.insert(INSERT, "Operation : (¬B ∩ C)\nResult:" + str(s4))
            k += 1
        #### Step 5 ####
        elif (k == 4): 
            step_txt.delete(1.0, END)
            step_txt.insert(INSERT, "Operation : (A ∩ B) ∪ (C ∩ B)\nResult:" + str(s5))
            k += 1
        #### Step 6 ####
        elif (k == 5): 
            step_txt.delete(1.0, END)
            step_txt.insert(INSERT, "Operation : (¬A ∩ ¬B) ∪ (¬B ∩ C)\nResult:" + str(s6))
            k += 1
        #### Step 7 ####
        elif (k == 6):
            step_txt.delete(1.0, END)
            step_txt.insert(INSERT, "Operation : D = (A ∩ B) ∪ (C ∩ B) ∪ (¬A ∩ ¬B) ∪ (¬B ∩ C)\nResult:" + str(s7))
            k+=1
        else:
            k = 0
            step_txt.delete(1.0, END)

    wind_2 = Toplevel(root)
    wind_2.title("Window 2")
    wind_2.geometry("1200x575")
    wind_2.config(bg = "#00FF99")

    menu2_1 = Menu(wind_2)
    wind_2.config(menu = menu2_1)
    wind2menu = Menu(menu2_1)
    wind2menu.add_command(label = "Window 3", command = wind_3)
    wind2menu.add_command(label = "Window 4", command = wind_4)
    wind2menu.add_command(label = "Window 5", command = wind_5)
    menu2_1.add_cascade(label = "Windows", menu = wind2menu)

    sets_fr = LabelFrame(wind_2, text = "Sets", padx = 10, pady = 10, width = 14015, bg = "#66CC33")

    a_txt = Text(sets_fr, height = 3, width = 140, borderwidth = 3)
    a_txt.insert(INSERT, "A: " + str(A))
    a_txt["state"] = DISABLED
    a_txt.grid(row = 0, column = 0, padx = 10, pady = 5)

    b_txt = Text(sets_fr, height = 3, width = 140, borderwidth = 3)
    b_txt.insert(INSERT, "B: " + str(B))
    b_txt["state"] = DISABLED
    b_txt.grid(row = 1, column = 0, padx = 10, pady = 5)
    
    c_txt = Text(sets_fr, height = 3, width = 140, borderwidth = 3)
    c_txt.insert(INSERT, "C: " + str(C))
    c_txt["state"] = DISABLED
    c_txt.grid(row = 2, column = 0, padx = 10, pady = 5)

    sets_fr.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

    steps_fr = LabelFrame(wind_2, text = "Step by step", padx = 10, pady = 10, width = 140, bg = "#66CC33")

    d = Label(steps_fr, text = "D = (A ∩ B) ∪ (C ∩ B) ∪ (¬A ∩ ¬B) ∪ (¬B ∩ C)", padx = 10, pady = 5, bg = "#66CC33")
    d.grid(row = 0, column = 0, columnspan = 4, padx = 15, pady = 15)

    # (A ∩ B) ∪ (C ∩ B) ∪ (¬A ∩ ¬B) ∪ (¬B ∩ C)
    
    step_txt = Text(steps_fr, height = 7, width = 140, borderwidth = 3)
  
    step_txt.grid(row = 1, column = 0, padx = 10, pady = 5)

    steps_fr.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 10)

    step_b = Button(wind_2, text = "Next step", width = 75, command = step, bg = "#009933")
    step_b.grid(row = 9, column = 0, columnspan = 2, padx = 10, pady = 10)

    save_b = Button(wind_2, text = "Save", width = 75, bg = "#009933", command = save)
    save_b.grid(row = 9, column = 2, columnspan = 2, padx = 10, pady = 10)

#### Window 3 ####
def wind_3():

    global A
    global B
    global C
    U = set([i for i in range(int(min_en.get()), int(max_en.get()) + 1)])
    s1 = set(U - (A.symmetric_difference(B)))
    s2 = set(C | s1)
    
    def save():
        global D
        with open(r"D2.txt", "w", encoding="utf-8") as w:
            w.write(str(step_txt.get(2.7, END)))
    def step():
        global l

        #### Step 1 ####
        if (l == 0): 
            step_txt.delete(1.0, END)
            step_txt.insert(INSERT, "Operation : ¬(A △ B)\nResult:" + str(s1))
            l += 1
        #### Step 2 ####
        elif (l == 1): 
            step_txt.delete(1.0, END)
            step_txt.insert(INSERT, "Operation : D = C ∪ ¬(A △ B)\nResult:" + str(s2))
            l += 1
        else:
            l = 0
            step_txt.delete(1.0, END)

    wind_3 = Toplevel(root)
    wind_3.title("Window 3")
    wind_3.geometry("1200x575")
    wind_3.config(bg = "#00FF99")

    menu3 = Menu(wind_3)
    wind_3.config(menu = menu3)
    wind3menu = Menu(menu3)
    wind3menu.add_command(label = "Window 2", command= wind_2)
    wind3menu.add_command(label = "Window 4", command= wind_4)
    wind3menu.add_command(label = "Window 5", command= wind_5)
    menu3.add_cascade(label = "Windows", menu = wind3menu)

    sets_fr = LabelFrame(wind_3, text = "Sets", padx = 10, pady = 10, width = 140, bg = "#66CC33")

    a_txt = Text(sets_fr, height = 3, width = 140, borderwidth = 3)
    a_txt.insert(INSERT, "A: " + str(A))
    a_txt["state"] = DISABLED
    a_txt.grid(row = 0, column = 0, padx = 10, pady = 5)

    b_txt = Text(sets_fr, height = 3, width = 140, borderwidth = 3)
    b_txt.insert(INSERT, "B: " + str(B))
    b_txt["state"] = DISABLED
    b_txt.grid(row = 1, column = 0, padx = 10, pady = 5)
    
    c_txt = Text(sets_fr, height = 3, width = 140, borderwidth = 3)
    c_txt.insert(INSERT, "C: " + str(C))
    c_txt["state"] = DISABLED
    c_txt.grid(row = 2, column = 0, padx = 10, pady = 5)

    sets_fr.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

    steps_fr = LabelFrame(wind_3, text = "Step by step", padx = 10, pady = 10, width = 140, bg = "#66CC33")

    d = Label(steps_fr, text = "D = C ∪ ¬(A △ B)", padx = 10, pady = 5, bg = "#66CC33")
    d.grid(row = 0, column = 0, columnspan = 4, padx = 15, pady = 15)

    # C ∪ ¬(A △ B)
    
    step_txt = Text(steps_fr, height = 7, width = 140, borderwidth = 3)
  
    step_txt.grid(row = 1, column = 0, padx = 10, pady = 5)

    steps_fr.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 10)

    step_b = Button(wind_3, text = "Next step", width = 75, command = step, bg = "#009933")
    step_b.grid(row = 9, column = 0, columnspan = 2, padx = 10, pady = 10)

    save_b = Button(wind_3, text = "Save", width = 75, bg = "#009933", command = save)
    save_b.grid(row = 9, column = 2, columnspan = 2, padx = 10, pady = 10)

#### Window 4 ####
def wind_4():

    U = set([i for i in range(int(min_en.get()), int(max_en.get()) + 1)])
    X = set()
    Y = set()
    Z = set()

    def show():
        z_txt.insert(INSERT, "Z: " + str(Z))
        z_txt["state"] = DISABLED
    def save():
        global Z
        with open(r"Z.txt", "w", encoding="utf-8") as w:
            w.write(str(z_txt.get(1.3, END)))

    for i in U:
        if i in A:
            X.add(i)
    # X = A

    for i in U:
        if i not in B:
            Y.add(i)
    # Y = ¬B 

    for i in U:
        if (i in X) or (i in Y):
            Z.add(i)
    # Z = X ∪ Y


    wind_4 = Toplevel(root)
    wind_4.title("Window 4")
    wind_4.geometry("1200x450")
    wind_4.config(bg = "#00FF99")

    menu4 = Menu(wind_4)
    wind_4.config(menu = menu4)
    wind4menu = Menu(menu4)
    wind4menu.add_command(label = "Window 2", command = wind_2)
    wind4menu.add_command(label = "Window 3", command = wind_3)
    wind4menu.add_command(label = "Window 5", command = wind_5)
    menu4.add_cascade(label = "Windows", menu = wind4menu)

    xy_fr = LabelFrame(wind_4, text = "X and Y sets", padx = 10, pady = 10, width = 140, bg = "#66CC33")

    x_txt = Text(xy_fr, height = 3, width = 140, borderwidth = 3)
    x_txt.insert(INSERT, "X = A:\n" + str(X))
    x_txt["state"] = DISABLED
    x_txt.grid(row = 0, column = 0, padx = 10, pady = 5)

    y_txt = Text(xy_fr, height = 3, width = 140, borderwidth = 3)
    y_txt.insert(INSERT, "Y = ¬B:\n" + str(Y))
    y_txt["state"] = DISABLED
    y_txt.grid(row = 1, column = 0, padx = 10, pady = 5)    

    xy_fr.grid(row = 0, column = 0, columnspan = 4, padx = 15, pady = 15)

    z_fr = LabelFrame(wind_4, text = "Z set", padx = 10, pady = 10, width = 140, bg = "#66CC33")

    z = Label(z_fr, text = "Z = X ∪ Y", padx = 5, pady = 5, bg = "#66CC33")
    z.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

    z_txt = Text(z_fr, height = 3, width = 140, borderwidth = 3)
    
    z_txt.grid(row = 1, column = 0, padx = 10, pady = 5)

    z_b = Button(wind_4, text = "Show Z", width = 75, command = show, bg = "#009933")
    z_b.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10)

    save_b = Button(wind_4, text = "Save", width = 75, bg = "#009933", command = save)
    save_b.grid(row = 2, column = 2, columnspan = 2, padx = 10, pady = 10)
    z_fr.grid(row = 1, column = 0, columnspan = 4, padx = 15, pady = 15)

#### Window 5 ####
def wind_5():

    def d1():
        with open(r"D1.txt", "r", encoding="utf-8") as w:
            d1_txt.insert(INSERT, w.read())
        d1_txt["state"] = DISABLED
    def d2():
        with open(r"D2.txt", "r", encoding="utf-8") as w:
            d2_txt.insert(INSERT, w.read())
        d2_txt["state"] = DISABLED
    def d_compare():
        if (list(d1_txt.get(1.0,END)) == list(d2_txt.get(1.0,END))):
            d_compare_txt.delete(1.0,END)
            d_compare_txt.insert(INSERT, "Sets D1 and D2 are EQUAL")
        else:
            d_compare_txt.delete(1.0, END)
            d_compare_txt.insert(INSERT, "Sets D1 and D2 are NOT EQUAL")

    def z1():
        with open(r"Z.txt", "r", encoding="utf-8") as w:
            z1_txt.insert(INSERT, w.read())
        z1_txt["state"] = DISABLED
    def z2():
        global A
        global B
        U = set([i for i in range(int(min_en.get()), int(max_en.get()) + 1)])
        X = set(A)
        Y = set(U.difference(B))
        Z2 = set(X.union(Y))
        z2_txt.delete(1.0, END)
        z2_txt.insert(INSERT, Z2)
        z2_txt["state"] = DISABLED

    def z_compare():
        if (list(z1_txt.get(1.0,END)) == (list(z2_txt.get(1.0,END) + "\n"))):
            z_compare_txt.delete(1.0,END)
            z_compare_txt.insert(INSERT, "Sets Z1 and Z2 are EQUAL")
        else:
            z_compare_txt.delete(1.0, END)
            z_compare_txt.insert(INSERT, "Sets Z1 and Z2 are NOT EQUAL")

    wind_5 = Toplevel(root)
    wind_5.title("Window 5")
    wind_5.geometry("1200x500")
    wind_5.config(bg = "#00FF99")

    menu5 = Menu(wind_5)
    wind_5.config(menu = menu5)
    wind5menu = Menu(menu5)
    wind5menu.add_command(label = "Window 2", command = wind_2)
    wind5menu.add_command(label = "Window 3", command = wind_3)
    wind5menu.add_command(label = "Window 4", command = wind_4)
    menu5.add_cascade(label = "Windows", menu = wind5menu)

    d_comp = LabelFrame(wind_5, text = "D sets comparison", width = 140, padx = 10, pady = 10, bg = "#66CC33")

    d1_b = Button(d_comp, text = "Show D1", width = 20, bg = "#009933", command = d1)
    d1_b.grid(row = 1, column = 0, padx = 10, pady = 10)

    d1_txt = Text(d_comp, height = 3, width = 120, borderwidth = 3)    
    d1_txt.grid(row = 0, rowspan = 3, column = 1, columnspan = 3, padx = 10, pady = 5)

    d2_b = Button(d_comp, text = "Show D2", width = 20, bg = "#009933", command = d2)
    d2_b.grid(row = 4, column = 0, padx = 10, pady = 10)

    d2_txt = Text(d_comp, height = 3, width = 120, borderwidth = 3)
    d2_txt.grid(row = 3, rowspan = 3, column = 1, columnspan = 3, padx = 10, pady = 5)

    d_compare = Button(d_comp, text = "Compare D1 and D2", width = 70, bg = "#009933", command = d_compare)
    d_compare.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10)

    d_compare_txt = Text(d_comp, height = 1, width = 70, borderwidth = 3)
    d_compare_txt.grid(row = 6, column = 2, columnspan = 2, padx = 10, pady = 10)

    d_comp.grid(row = 0, rowspan = 6, column = 0, columnspan = 4, padx = 10, pady = 10)

    z_comp = LabelFrame(wind_5, text = "Z sets comparison", width = 140, padx = 10, pady = 10, bg = "#66CC33")

    z1_b = Button(z_comp, text = "Show Z1", width = 20, bg = "#009933", command = z1)
    z1_b.grid(row = 1, column = 0, padx = 10, pady = 10)

    z1_txt = Text(z_comp, height = 3, width = 120, borderwidth = 3)    
    z1_txt.grid(row = 0, rowspan = 3, column = 1, columnspan = 3, padx = 10, pady = 5)

    z2_b = Button(z_comp, text = "Show Z2", width = 20, bg = "#009933", command = z2)
    z2_b.grid(row = 4, column = 0, padx = 10, pady = 10)

    z2_txt = Text(z_comp, height = 3, width = 120, borderwidth = 3)
    z2_txt.grid(row = 3, rowspan = 3, column = 1, columnspan = 3, padx = 10, pady = 5)

    z_compare = Button(z_comp, text = "Compare Z1 and Z2", width = 70, bg = "#009933", command = z_compare)
    z_compare.grid(row = 6, column = 0, columnspan = 2, padx = 10, pady = 10)

    z_compare_txt = Text(z_comp, height = 1, width = 70, borderwidth = 3)
    z_compare_txt.grid(row = 6, column = 2, columnspan = 2, padx = 10, pady = 10)

    z_comp.grid(row = 6, rowspan = 6, column = 0, columnspan = 4, padx = 10, pady = 10)

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
    group_n["text"] = "My group: ", M + "-", G
    num["text"] = "My number:", N
    if M == "ІО": N += 2
    var["text"] = "My variant:", (N + G % 60) % 30 + 1

def u_set():
    global U
    if (((min_en.get()).isnumeric() == True) and (max_en.get()).isnumeric() == True):
        U = set(range(int(min_en.get()), int(max_en.get()) + 1))
    else: messagebox.showerror("ValueError", "Please enter integer value!")        

def cardA():
    global card_A
    card_A = a_card.get()
def cardB():
    global card_B
    card_B = b_card.get()
def cardC():
    global card_C
    card_C = c_card.get()

def rand_A():
    global A
    global U
    A = set([i for i in random.sample(U, int(card_A))])        
    a_rand.delete(1.0, END)
    a_rand.insert(INSERT, A)
    manual_fr.config(bg = "#CC0000")
    man_a_but.config(bg = "#FF0000")
    man_b_but.config(bg = "#FF0000")
    man_c_but.config(bg = "#FF0000")
    man_a_but["state"] = DISABLED
    man_b_but["state"] = DISABLED
    man_c_but["state"] = DISABLED
    a_man["state"] = DISABLED
    b_man["state"] = DISABLED
    c_man["state"] = DISABLED
def rand_B():
    global B
    global U
    B = set([i for i in random.sample(U, int(card_B))])
    b_rand.delete(1.0, END)
    b_rand.insert(INSERT, B)
    manual_fr.config(bg = "#CC0000")
    man_a_but.config(bg = "#FF0000")
    man_b_but.config(bg = "#FF0000")
    man_c_but.config(bg = "#FF0000")
    man_a_but["state"] = DISABLED
    man_b_but["state"] = DISABLED
    man_c_but["state"] = DISABLED
    a_man["state"] = DISABLED
    b_man["state"] = DISABLED
    c_man["state"] = DISABLED
def rand_C():
    global C
    global U
    C = set([i for i in random.sample(U, int(card_C))])
    c_rand.delete(1.0, END)
    c_rand.insert(INSERT, C)
    manual_fr.config(bg = "#CC0000")
    man_a_but.config(bg = "#FF0000")
    man_b_but.config(bg = "#FF0000")
    man_c_but.config(bg = "#FF0000")
    man_a_but["state"] = DISABLED
    man_b_but["state"] = DISABLED
    man_c_but["state"] = DISABLED
    a_man["state"] = DISABLED
    b_man["state"] = DISABLED
    c_man["state"] = DISABLED

def get_A():
    global A
    for i in (a_man.get()).split():
        if (i.isnumeric() == True):
            i = int(i)
            A.add(i)
            rand_fr.config(bg = "#CC0000")
            rand_a_but.config(bg = "#FF0000")
            rand_b_but.config(bg = "#FF0000")
            rand_c_but.config(bg = "#FF0000")
            a_rand["state"] = DISABLED
            b_rand["state"] = DISABLED
            c_rand["state"] = DISABLED
            rand_a_but["state"] = DISABLED
            rand_b_but["state"] = DISABLED
            rand_c_but["state"] = DISABLED
        else: messagebox.showerror("ValueError", "Please enter integer value!") 
def get_B():
    global B
    for i in (b_man.get()).split():
        if (i.isnumeric() == True):
            i = int(i)
            B.add(i)
            rand_fr.config(bg = "#CC0000")
            rand_a_but.config(bg = "#FF0000")
            rand_b_but.config(bg = "#FF0000")
            rand_c_but.config(bg = "#FF0000")
            a_rand["state"] = DISABLED
            b_rand["state"] = DISABLED
            c_rand["state"] = DISABLED
            rand_a_but["state"] = DISABLED
            rand_b_but["state"] = DISABLED
            rand_c_but["state"] = DISABLED
        else: messagebox.showerror("ValueError", "Please enter integer value!")
def get_C():
    global C
    for i in (c_man.get()).split():
        if (i.isnumeric() == True):
            i = int(i)
            C.add(i)
            rand_fr.config(bg = "#CC0000")
            rand_a_but.config(bg = "#FF0000")
            rand_b_but.config(bg = "#FF0000")
            rand_c_but.config(bg = "#FF0000")
            a_rand["state"] = DISABLED
            b_rand["state"] = DISABLED
            c_rand["state"] = DISABLED
            rand_a_but["state"] = DISABLED
            rand_b_but["state"] = DISABLED
            rand_c_but["state"] = DISABLED
        else: messagebox.showerror("ValueError", "Please enter integer value!")

#### Menu ####
menubar = Menu(root)
windowmenu = Menu(menubar, tearoff = 0)
root.config(menu = menubar)
windowmenu.add_separator()
windowmenu.add_command(label = "Window 2", command = wind_2)
windowmenu.add_command(label = "Window 3", command = wind_3)
windowmenu.add_command(label = "Window 4", command = wind_4)
windowmenu.add_command(label = "Window 5", command = wind_5)
menubar.add_cascade(label = "Windows", menu = windowmenu)

#### Info ####
info_fr = LabelFrame(root, text = "Student Info", padx = 15, pady = 15, bg = "#CC0000")
info_b = Button(info_fr, text = "Show info", width = 90, command = inf, bg = "#FF0000")

info_b.grid(row = 0, column = 0, columnspan = 2)
info_fr.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

#### Cardinality ####
card_fr = LabelFrame(root, text = "Cardinality", padx = 15, pady = 15, bg = "#66CC33")

a_card = Scale(card_fr, from_ = 0, to = 200, orient = HORIZONTAL, length = 300, bg = "#009933")
b_card = Scale(card_fr, from_ = 0, to = 200, orient = HORIZONTAL, length = 300, bg = "#009933")
c_card = Scale(card_fr, from_ = 0, to = 200, orient = HORIZONTAL, length = 300, bg = "#009933")

a_button = Button(card_fr, text = "Approve set A", width = 45, command = cardA, bg = "#009933")
b_button = Button(card_fr, text = "Approve set B", width = 45, command = cardB, bg = "#009933")
c_button = Button(card_fr, text = "Approve set C", width = 45, command = cardC, bg = "#009933")

a_button.grid(row = 0, column = 1)
b_button.grid(row = 1, column = 1)
c_button.grid(row = 2, column = 1)

a_card.grid(row = 0, column = 0, padx = 5)
b_card.grid(row = 1, column = 0, padx = 5)
c_card.grid(row = 2, column = 0, padx = 5)
card_fr.grid(row = 1, column = 0, columnspan = 2, padx = 10, pady = 10)

#### Universal Set ####

univ_fr = LabelFrame(root, text = "Universal Set", padx = 15, pady = 24, height = 100, bg = "#66CC33")

univ_b = Button(univ_fr, text = "Accept\nboundries", width = 30, bg = "#009933", command = u_set)

univ_b.grid(row = 0, rowspan = 2, column = 0)

min_en = Entry(univ_fr, width = 5)
max_en = Entry(univ_fr, width = 5)

min_en.grid(row = 0, column = 1, padx = 15)
max_en.grid(row = 1, column = 1, padx = 15)
univ_fr.grid(row = 0, column = 3, padx = 10, pady = 10)

#### Random ####

rand_fr = LabelFrame(root, text = "Random", padx = 15, pady = 15, bg = "#66CC33")

rand_a_but = Button(rand_fr, text = "Generate set A", width = 25, command = rand_A, bg = "#009933")
rand_b_but = Button(rand_fr, text = "Generate set B", width = 25, command = rand_B, bg = "#009933")
rand_c_but = Button(rand_fr, text = "Generate set C", width = 25, command = rand_C, bg = "#009933")

rand_a_but.grid(row = 0, column = 0, padx = 5, pady = 2)
rand_b_but.grid(row = 1, column = 0, padx = 5, pady = 2)
rand_c_but.grid(row = 2, column = 0, padx = 5, pady = 2)

a_rand = Text(rand_fr, height = 1, width = 55, borderwidth = 3)
b_rand = Text(rand_fr, height = 1, width = 55, borderwidth = 3)
c_rand = Text(rand_fr, height = 1, width = 55, borderwidth = 3)

a_rand.grid(row = 0, column = 1)
b_rand.grid(row = 1, column = 1)
c_rand.grid(row = 2, column = 1)

rand_fr.grid(row = 2, column = 0, padx = 10, pady = 10)

#### Manualy ####

manual_fr = LabelFrame(root, text = "Manually", padx = 15, pady = 15, bg = "#66CC33")

man_a_but = Button(manual_fr, text = "Approve set A", width = 20, command = get_A, bg = "#009933")
man_b_but = Button(manual_fr, text = "Approve set B", width = 20, command = get_B, bg = "#009933")
man_c_but = Button(manual_fr, text = "Approve set C", width = 20, command = get_C, bg = "#009933")

man_a_but.grid(row = 0, column = 3, padx = 5, pady = 2)
man_b_but.grid(row = 1, column = 3, padx = 5, pady = 2)
man_c_but.grid(row = 2, column = 3, padx = 5, pady = 2)

a_man = Entry(manual_fr, width = 40, borderwidth = 3)
b_man = Entry(manual_fr, width = 40, borderwidth = 3)
c_man = Entry(manual_fr, width = 40, borderwidth = 3)

a_man.grid(row = 0, column = 4)
b_man.grid(row = 1, column = 4)
c_man.grid(row = 2, column = 4)

manual_fr.grid(row = 2, column = 3, columnspan = 2, padx = 10, pady = 10)

root.mainloop()
