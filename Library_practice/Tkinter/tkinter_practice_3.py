# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 01:55:21 2021

@author: 박민규
"""


import tkinter as tk

#%% run main gui
gui = tk.Tk()

#%% define functions
def my_click():
    user_msg = "You typed:"+my_entry.get()
    my_label = tk.Label(gui,text=user_msg)
    my_label.pack()

#%%create entry 
my_entry =tk.Entry(gui,width=50)
my_entry.pack()
my_entry.insert(0,'Enter values')
# create button
my_button = tk.Button(gui,text='Click',padx=30,pady=20,
                      command=my_click) 


# place in gui
my_button.pack()



# run mainloop
gui.mainloop()
