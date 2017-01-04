#!python2
# GUI.py
from Tkinter import *
import tkMessageBox
class App:
    #Constructor
    def __init__(self, param):
        
        #Label : First Name
        Label(param, text="First Name").grid(row=0)
        self.e1=Entry(param)
        self.e1.grid(row=0, column=1)

        #Label : Last Name
        Label(param, text="Last Name").grid(row=1)
        self.e2=Entry(param)
        self.e2.grid(row=1, column=1)

        #Label : Age
        Label(param, text="Age").grid(row=2)
        self.e3=Entry(param)
        self.e3.grid(row=2, column=1)

        #Blank Label
        Label(param, text="", width=5).grid(row=0, column=3)

        #Label : Gender
        Label(param, text="Gender").grid(row=0, column=4)
        self.f1=Frame(param, relief= "sunken", bd=2)
        self.v=IntVar()
        #Radiobuttons : Male & Female
        self.r1=Radiobutton(self.f1, text="Male", variable=self.v, value=1).pack(anchor=W)
        self.r2=Radiobutton(self.f1, text="Female", variable=self.v, value=2).pack(anchor=W)
        self.f1.grid(row=1, column=4)

        #Blank Label
        Label(param, text="").grid(row=3) 

        #Course you want to apply :
        Label(param, text="Course Applied for:", wraplength=60).grid(row=4) #, column=3)
        self.L1 = Listbox(param, width = 30, exportselection=0, height = 4)
        for item in ["Advanced Machine Learning", "Advanced NLP", "Advanced Artificial Intelligence", "Virtual Reality"]:
            self.L1.insert(END, item)
        self.L1.grid(row=4, column=1)     

        #Buttons
        self.f2=Frame(param)
        #B1
        self.w=Button(self.f2, text ="Prerequisite Courses", height =1, width=15, command=self.Check_Prerequisites, default=ACTIVE).pack()
        #B2
        self.w1=Button(self.f2, text ="Clear", height =1, width=15, command=self.Clear).pack()
        #B3
        self.w2=Button(self.f2, text ="Close", height=1, width=15, command=self.Close).pack()

        self.f2.grid(row=4, column=4)

        #Blank Label
        Label(param, text="").grid(row=6) 

        #Checkbox
        self.var=IntVar()
        self.c=Checkbutton(param , text="Part-Time Course", variable= self.var, offvalue=0, onvalue=1)
        self.c.grid(row=7)
           
    def Check_Prerequisites(self):   
        self.Eval()

    def Eval(self):

        self.fname = self.e1.get()
        self.lname = self.e2.get()
        self.age =  int(self.e3.get())

        #Check for Age
        if self.age < 21:
            tkMessageBox.showwarning("Students with age less than 21 are not eligible. Sorry!")
            return

        #Check for Gender
        if self.v.get()==1:
            self.str1 = "Dear Mr." 
        elif self.v.get()==2:
            self.str1 = "Dear Ms."
        else:
            tkMessageBox.showwarning("Missing Info", "Please select the appropriate gender")
            return

        #Check for Prerequisite Course
        self.name = self.str1 + " " + self.fname + " " + self.lname
            
        self.varl1 = self.L1.curselection()[0]

        print self.varl1
        if self.varl1 == 0:
            self.prereq = "The prerequisite for this course is Introduction to Machine Learning."
            self.flag = 1
        elif self.varl1 == 1:
            self.prereq = "The prerequisite for this course is Language Processors."
            self.flag = 1
        elif self.varl1 == 2:
            self.prereq = "The prerequisite for this course is Introduction to Artificial Intelligence."
            self.flag = 0
        else:
            self.prereq = "The prerequisite for this course is Computer Graphics."
            self.flag = 0
        
        #Check whether Part Time
        if self.var.get() == 1 and self.flag == 0:
            self.str2 = "\nThis course is not available part time."
        elif self.var.get() == 1 and self.flag == 1:
            self.str2 = "\nThis course is available part time."
        else:
            self.str2 = ""

        self.result = self.prereq + self.str2
        tkMessageBox.showinfo(self.name, self.result)


    def Close(self):
        root.destroy()
        
    def Clear(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.c.deselect()
        self.L1.select_clear(self.L1.curselection())
        
root = Tk()
app = App(root)
root.mainloop()
