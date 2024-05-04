######################################################
##                  Angelo NICOLI 2024              ##
##                    LICENSE MIT                   ##
######################################################

from tkinter import *
from License_text import *
import math as mt

Ver = 0.9  # Software Version

#  Initialize Window
root = Tk()

Operation_text = [""]

operation_label = Label(root,text = "",bg="#3e3e42", borderwidth=1, width= 25, height=2,fg='white',anchor ='e')
e = Label(root, width= 25, bg="#3e3e42",fg='white',anchor ='e')


def Initialize_Window():
    root.title("Simple Calculator v" + str(Ver))
    root.geometry("300x600")
    root.configure(bg='#252526')
    # Crea la barra per gli input dei dati
    operation_label.grid(row=0, column=0,columnspan=3,padx = 10)
    e.grid(row=1, column=0, columnspan=3, padx = 10, pady=5, ipady=10)

    Term_List= {"First_Number": 0,"Second_Numer": 0,"Answer":0}
    print(Term_List["First_Number"])



def sin_text(p):
    global f_num
    global math
    math = "division"
    Operation_Log(str("mt.sin"))

def cos_text(p):
    global f_num
    global math
    math = "division"
    Operation_Log(str("mt.cos"))

def tan_text(p):
    global f_num
    global math
    math = "division"
    Operation_Log(str("mt.tan"))


        
def SciCalculator_Gui():
    button_sin =  Button(root, text="sin", padx=40, pady=20,bg="#3e3e42",fg='white', command=lambda: sin_text(1))
    button_sin.grid(row=2,column=40)

    button_cos =  Button(root, text="cos", padx=40, pady=20,bg="#3e3e42",fg='white', command=lambda: cos_text(1))
    button_cos.grid(row=3,column=40)

    button_tan =  Button(root, text="tan", padx=40, pady=20,bg="#3e3e42",fg='white', command=lambda: tan_text(1))
    button_tan.grid(row=4,column=40)


def change_gui():
    print("change")
    SciCalculator_Gui()
    root.geometry("400x600")

def return_gui():
    #button100[0].destroy()
    root.geometry("300x600")

# root.bind("b", return_gui)
# root.bind("a", change_gui)

def Show_License():
    openNewWindow(root)

# Operation Log 
def Operation_Log(new_content):
    Operation_text[0] += new_content
    operation_label.config(text = Operation_text[0])

def button_click(number):
    # e.delete(0,END) (Mostra un solo carattere alla volta)
    Operation_Log(str(number))
    #print(number)

def button_del():
    Operation_text[0] = ""
    operation_label.config(text = Operation_text[0])
    e.config(text="0.0")

def button_sum():
    global f_num
    global math
    math = "addition"
    Operation_Log(str("+"))

def button_subtraction():
    global f_num
    global math
    math = "subtraction"
    Operation_Log(str("-"))

def button_multiplication():
    global f_num
    global math
    math = "multiplication"
    Operation_Log(str("*"))

def button_division():
    global f_num
    global math
    math = "division"
    Operation_Log(str("/"))


def button_add_sqrt():
    global f_num
    global math
    math = "division"
    Operation_Log(str("mt.sqrt("))

 
def button_add_sin():
    global f_num
    global math
    math = "division"
    Operation_Log(str("mt.sqrt("))   

def button_add_cos():
    global f_num
    global math
    math = "division"
    Operation_Log(str("mt.sqrt("))  


def button_add_tan():
    global f_num
    global math
    math = "division"
    Operation_Log(str("mt.sqrt("))  


def button_add_power():
    global f_num
    global math
    pass  


def button_add_point():
    global f_num
    global math
    math = "division"
    Operation_Log(str("."))

def button_equals():
    global f_num
    global math
    
    print("Operation is" + Operation_text[0])
    print(Operation_text)
    print(type(Operation_text[0]))
    print(type("math.sqrt(9)"))
    
    a = "math.sqrt(9)"

    if Operation_text[0] != a:
        print("Different Value")
    else:
        print("Same Value")

    res = eval(Operation_text[0])
    print(res)
    e.config(text = str(res))


def Clear_Text(): 
    Operation_text[0] = ""
    operation_label.config(text = Operation_text[0])

def Menu_Bar():
    # Create Menu bar
    menubar = Menu(root)
    root.config(menu=menubar)

    # First Menu column
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)

    filemenu.add_command(label="New")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    # Second Menu column
    editmenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Mode", menu=editmenu)

    editmenu.add_command(label="Standard", command= return_gui )
    editmenu.add_command(label="Scientific", command= change_gui)

    # Third Menu column
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)

    helpmenu.add_command(label="Help Index")
    helpmenu.add_command(label="License", command = Show_License)

    # Fourth Menu column
    resmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Resolution", menu=resmenu)

    resmenu.add_command(label="Resolution: 800x600",command=res1)
    resmenu.add_command(label="Resolution: 1024x700",command=res2)
    resmenu.add_command(label="Resolution: 1400x750",command=res3)


def res1():
     root.geometry('{}x{}'.format(800,600))
     print("Resolution Changed")

def res2():
     root.geometry('{}x{}'.format(1024, 700))
     print("Resolution Changed")

def res3():
     root.geometry('{}x{}'.format(1400, 750))
     print("Resolution Changed")

def res4():
     root.geometry('{}x{}'.format(1400, 750))
     print("Resolution Changed")

def Calculator_Gui():

    Clear_Log =  Button(root, text="Clear Log",pady=20 , bg="#3e3e42",fg='white', command=Clear_Text)

    button_1 =  Button(root, text="1",pady=20 , bg="#3e3e42",fg='white', command=lambda: button_click(1))
    button_2 =  Button(root, text="2", pady=20, bg="#3e3e42",fg='white', command=lambda: button_click(2))
    button_3 =  Button(root, text="3", pady=20,bg="#3e3e42",fg='white', command=lambda: button_click(3))
    button_4 =  Button(root, text="4", pady=20,bg="#3e3e42",fg='white', command=lambda: button_click(4))
    button_5 =  Button(root, text="5", pady=20,bg="#3e3e42",fg='white', command=lambda: button_click(5))
    button_6 =  Button(root, text="6", pady=20,bg="#3e3e42",fg='white', command=lambda: button_click(6))
    button_7 =  Button(root, text="7", pady=20,bg="#3e3e42",fg='white', command=lambda: button_click(7))
    button_8 =  Button(root, text="8", pady=20,bg="#3e3e42",fg='white', command=lambda: button_click(8))
    button_9 =  Button(root, text="9", pady=20,bg="#3e3e42",fg='white', command=lambda: button_click(9))
    button_0 =  Button(root, text="0", pady=20,bg="#3e3e42",fg='white', command=lambda: button_click(0))

    button_Par_OPEN =  Button(root, text="(", padx=40, pady=20,bg="#3e3e42",fg='white', command=lambda: button_click("("))
    button_Par_OPEN.grid(row=9,column=0)

    button_Par_Cls =  Button(root, text=")", padx=40, pady=20,bg="#3e3e42",fg='white', command=lambda: button_click(")"))
    button_Par_Cls.grid(row=9,column=1)

    button_equal = Button(root, text="=",bg="#154020",fg='white', padx=91, pady=20, command=button_equals)
    button_clear = Button(root, text="Clear",bg="#561a27",fg='white', padx=80, pady=20, command=button_del)

    button_add = Button(root, text="+", bg="#043738",fg='white', padx=39, pady=19, command=button_sum)
    button_subtract = Button(root, text="-",bg="#043738",fg='white',  padx=40, pady=20, command= button_subtraction)
    button_multiply = Button(root, text="*",bg="#043738",fg='white',  padx=40, pady=20, command= button_multiplication)
    button_divide= Button(root, text="/",bg="#043738",fg='white',  padx=40, pady=20, command= button_division)

    button_sqrt= Button(root, text="√x",bg="#043738",fg='white',  padx=40, pady=20, command= button_add_sqrt)

    button_power= Button(root, text="x²",bg="#043738",fg='white',  padx=40, pady=20, command= button_division)

    button_point= Button(root, text=".",bg="#3e3e42",fg='white',  padx=40, pady=20, command= button_add_point)

    # Put the buttons on the screen

    button_1.grid(row=4,column=0, sticky=W+E)
    button_2.grid(row=4,column=1, sticky=W+E)
    button_3.grid(row=4,column=2, sticky=W+E)

    button_4.grid(row=3,column=0, sticky=W+E)
    button_5.grid(row=3,column=1, sticky=W+E)
    button_6.grid(row=3,column=2, sticky=W+E)

    button_7.grid(row=2,column=0, sticky=W+E)
    button_8.grid(row=2,column=1, sticky=W+E)
    button_9.grid(row=2,column=2, sticky=W+E)

    button_0.grid(row=5,column=0, sticky=W+E)

    button_clear.grid(row=5,column=1,columnspan=2, sticky=W+E)
    button_equal.grid(row=6,column=1,columnspan=2, sticky=W+E)
    button_point.grid(row=6,column=0,sticky=W+E)

    button_add.grid(row=8,column=0)
    button_subtract.grid(row=7,column=0)
    button_multiply.grid(row=7,column=1)
    button_divide.grid(row=7,column=2)

    button_sqrt.grid(row=8,column=2)
    button_power.grid(row=8,column=1)

    Clear_Log.grid(row=9,column=2, sticky=W+E)


Initialize_Window()
Menu_Bar()
Calculator_Gui()

#print(Operation_text[0])

root.mainloop()
