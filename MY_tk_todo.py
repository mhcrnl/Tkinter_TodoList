#!/usr/bin/env python
# coding: utf-8

#import tkinter as tk
from tkinter import *

class ClassName(tk.Frame):
    """Documentation for ClassName

    """
    def __init__(self, master):
        super().__init__(master)

        self.master.title("TODO APP")
        self.master.geometry("750x650")
        
        self.cont = tk.Listbox(master, font="Georgia 20 bold", bg="Silver")
        self.tas =tk.StringVar()
        self.user_in = tk.Entry(master, font="Georgia 20", textvariable=self.tas,
                           bg="pink")

        #add_fun = lambda content=cont, task=tas : content.insert(END, task.get())
       # del_fun = lambda content=self.cont : content.delete(ANCHOR)

        btn_add = tk.Button(master, text="ADAUGA", font="Arial 20",
                            command=self.add_fun, bg="Green", fg="White",
                            padx=20)

        btn_del = tk.Button(master, text="STERGE", font="Arial 20",
                            command=self.del_fun, bg="Red", fg="White")
        
        self.cont.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        self.user_in.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        btn_add.grid(row=2, column=0)
        btn_del.grid(row=2, column=1)
        
        #self.pack()


    def add_fun(self):
        self.cont.insert(END, self.tas.get())

    def del_fun(self):
        self.cont.delete(ANCHOR)
        

root = tk.Tk()
root.title("TODO_APP")
todoapp = ClassName(root)
todoapp.mainloop()
