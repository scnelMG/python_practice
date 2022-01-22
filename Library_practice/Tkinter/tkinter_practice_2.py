# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 01:47:30 2021

@author: 박민규
"""

import tkinter as tk

# run main gui
gui = tk.Tk()

# define function
def my_click():
    my_label=tk.Label(gui, text='Button Clicked!')
    my_label.pack()


# create button
my_button = tk.Button(gui,text='Click',padx=30,pady=20,
                      command=my_click) 
                    #state=tk.DISABLED 추가시 버튼 사용 X

# place in gui
my_button.pack()





# run mainloop
gui.mainloop()
