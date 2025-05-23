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

Text_Script = [""]   # Text used by script to evaluate operations
Text_User = [""]     # Text seen by the user (Displayed by GUI)

Label_Text = Label(root,text = "",bg="#3e3e42", borderwidth=1, width= 25, height=2,fg='white',anchor ='e')   #Label (Displayed by GUI)
Result_Text = Label(root, width= 25, bg="#3e3e42",fg='white',anchor ='e')


# Operation Log 
def Operation_Log(new_content):
    Text_Script[0] += new_content
    Label_Text.config(text = Text_Script[0])
    print(Text_Script[0])

def button_click(number):
    Operation_Log(str(number))

def Add_Operator(number,displayed = ""):
    Operation_Log(str(number))

def button_del():
    Text_Script[0] = ""
    Label_Text.config(text = Text_Script[0])
    Result_Text.config(text="0.0")

def button_equals():
    res = eval(Text_Script[0])
    #print(res)
    Result_Text.config(text = str(res))

def Clear_Text(): 
    Text_Script[0] = ""
    Label_Text.config(text = Text_Script[0])


# Software License
def Show_License():
    openNewWindow(root)

def Initialize_Window():
    root.title("Simple Calculator v" + str(Ver))
    root.geometry("300x600")
    root.configure(bg='#252526')

    # Input Bar
    Label_Text.grid(row=0, column=0,columnspan=3,padx = 10)
    Result_Text.grid(row=1, column=0, columnspan=3, padx = 10, pady=5, ipady=10)

    Term_List= {"First_Number": 0,"Second_Numer": 0,"Answer":0}
    print(Term_List["First_Number"])

def Scientific_Gui():
    print("change")
    SciCalculator_Gui()
    root.geometry("400x600")

def Classic_Gui():
    root.geometry("300x600")

# Create Menu bar
def Menu_Bar():   
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

    editmenu.add_command(label="Standard", command= Classic_Gui)
    editmenu.add_command(label="Scientific", command= Scientific_Gui)

    # Third Menu column
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)

    helpmenu.add_command(label="Help Index")
    helpmenu.add_command(label="License", command = Show_License)

    # Fourth Menu column
    resmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Resolution", menu=resmenu)
    resmenu.add_command(label="Resolution: 300x600", command=lambda: res(300,600))
    resmenu.add_command(label="Resolution: 400x600", command=lambda: res(400,600))
    resmenu.add_command(label="Resolution: 800x600", command=lambda: res(800,600))
    resmenu.add_command(label="Resolution: 1024x700", command=lambda: res(1024, 700))
    resmenu.add_command(label="Resolution: 1400x750", command=lambda: res(1400, 750))

def res(a,b):
     root.geometry('{}x{}'.format(a,b))
     print("Resolution Changed")


def Calculator_Gui():
    # Define Buttons
    Clear_Log = Button(root, text="Clear Log",pady=20 , bg="#3e3e42",fg='white', command=Clear_Text)
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
    button_Par_OPEN =  Button(root, text=" ( ", padx=40, pady=20,bg="#3e3e42",fg='white', command=lambda: button_click("("))
    button_Par_OPEN.grid(row=9,column=0)
    button_Par_Cls =  Button(root, text=" ) ", padx=40, pady=20,bg="#3e3e42",fg='white', command=lambda: button_click(")"))
    button_Par_Cls.grid(row=9,column=1)
    button_equal = Button(root, text="=",bg="#154020",fg='white', padx=91, pady=20, command=button_equals)
    button_clear = Button(root, text="Clear",bg="#561a27",fg='white', padx=80, pady=20, command=button_del)
    button_add = Button(root, text=" + ", bg="#043738",fg='white', padx=39, pady=19,  command=lambda: Add_Operator("+"))
    button_subtract = Button(root, text=" - ",bg="#043738",fg='white',  padx=40, pady=20, command=lambda: Add_Operator("-"))
    button_multiply = Button(root, text=" * ",bg="#043738",fg='white',  padx=40, pady=20, command=lambda: Add_Operator("*"))
    button_divide= Button(root, text=" /  ",bg="#043738",fg='white',  padx=40, pady=20, command=lambda: Add_Operator("/"))
    button_sqrt= Button(root, text="√x",bg="#043738",fg='white',  padx=40, pady=20, command=lambda: Add_Operator("mt.sqrt("))  
    button_power= Button(root, text="x²",bg="#043738",fg='white',  padx=40, pady=20, command=lambda: Add_Operator("**"))
    button_point= Button(root, text=".",bg="#3e3e42",fg='white',  padx=40, pady=20,  command=lambda: Add_Operator("."))

    # Buttons Position on screen

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

def SciCalculator_Gui():
    # Define Buttons

    button_sin =  Button(root, text="sin", padx=40, pady=20,bg="#3e3e42",fg='white',  command=lambda: Add_Operator("mt.sin("))  
    button_cos =  Button(root, text="cos", padx=40, pady=20,bg="#3e3e42",fg='white', command=lambda: Add_Operator("mt.cos("))
    button_tan =  Button(root, text="tan", padx=40, pady=20,bg="#3e3e42",fg='white', command=lambda: Add_Operator("mt.tan(")) 
    button_exp=  Button(root, text="exp", padx=40, pady=20,bg="#3e3e42",fg='white', command=lambda: Add_Operator("mt.exp("))
    button_fact=  Button(root, text="fact", padx=40, pady=20,bg="#3e3e42",fg='white', command=lambda: Add_Operator("mt.factorial("))
    button_const_e=  Button(root, text="e   ", padx=40, pady=20,bg="#23395d",fg='white', command=lambda: Add_Operator("mt.e"))
    button_const_pi =  Button(root, text="π   ", padx=40, pady=20,bg="#23395d",fg='white', command=lambda: Add_Operator("mt.pi"))

    # Buttons Position on screen

    button_sin.grid(row=2,column=40)
    button_cos.grid(row=3,column=40)
    button_tan.grid(row=4,column=40)    
    button_exp.grid(row=5,column=40)
    button_exp.grid(row=5,column=40)
    button_fact.grid(row=6,column=40)
    button_const_e.grid(row=7,column=40)
    button_const_pi.grid(row=8,column=40)


def Run_Window():
    Initialize_Window()
    Menu_Bar()
    Calculator_Gui()

# Start GUI
Run_Window()

root.mainloop()
