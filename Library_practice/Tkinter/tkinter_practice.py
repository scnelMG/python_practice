# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 01:39:19 2021

@author: 박민규
"""

import tkinter as tk

# run main gui
gui = tk.Tk()

# create labels
my_label_1 = tk.Label(gui, text='Hello World!')
my_label_2 = tk.Label(gui, text='안녕!')

# place in gui
#my_label_1.pack()
#my_label_2.pack()
my_label_1.grid(row=0,column=0)
my_label_2.grid(row=1,column=0)





# run mainloop
gui.mainloop()








































