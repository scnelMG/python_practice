# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 02:56:30 2021

@author: 박민규
"""

#%% import libraries
import tkinter as tk

#%%  start main gui
gui = tk.Tk()
gui.title('My GUI Calculator')
#%% define functions
def button_click(number):
    cur_num = entry_box.get()
    entry_box.delete(0,tk.END)
    entry_box.insert(0,str(cur_num) +str(number)) #가장 마지막에 누른 숫자가 제일 오른쪽에 나오도록
    
def button_clear():
    entry_box.delete(0,tk.END)
    
def button_add():
    first_num = entry_box.get()
    global g_first_num
    global g_operation
    g_operation = 'add'
    g_first_num =int(first_num)
    entry_box.delete(0,tk.END)
    
def button_subtract():
    first_num = entry_box.get()
    global g_first_num
    global g_operation
    g_operation = 'subtract'
    g_first_num =int(first_num)
    entry_box.delete(0,tk.END)
    
def button_multiply():
    first_num = entry_box.get()
    global g_first_num
    global g_operation
    g_operation = 'multiply'
    g_first_num =int(first_num)
    entry_box.delete(0,tk.END)
    
def button_divide():
    first_num = entry_box.get()
    global g_first_num
    global g_operation
    g_operation = 'divide'
    g_first_num =int(first_num)
    entry_box.delete(0,tk.END)
    
def button_equal():
    second_num=entry_box.get()
    entry_box.delete(0,tk.END)
    if g_operation == 'add':
        result = g_first_num + int(second_num)
        entry_box.insert(0,result)
    elif g_operation == 'subtract':
        result = g_first_num - int(second_num)
        entry_box.insert(0,result)
    elif g_operation == 'multiply':
        result = g_first_num * int(second_num)
        entry_box.insert(0,result)
    elif g_operation == 'divide':
        result = g_first_num / int(second_num)
        entry_box.insert(0,result)
    
    
    
    
    
    
#%% create entry box
entry_box = tk.Entry(gui, width=30, borderwidth=5)
entry_box.grid(row=0,column=0,columnspan=4,padx=40,pady=1) #columnspan 차지하는 column 수

#%% create button

button_0 = tk.Button(gui,text='0',padx=25,pady=15,command = lambda: button_click(0))
button_1 = tk.Button(gui,text='1',padx=25,pady=15,command = lambda: button_click(1))
button_2 = tk.Button(gui,text='2',padx=25,pady=15,command = lambda: button_click(2))
button_3 = tk.Button(gui,text='3',padx=25,pady=15,command = lambda: button_click(3))
button_4 = tk.Button(gui,text='4',padx=25,pady=15,command = lambda: button_click(4))
button_5 = tk.Button(gui,text='5',padx=25,pady=15,command = lambda: button_click(5))
button_6 = tk.Button(gui,text='6',padx=25,pady=15,command = lambda: button_click(6))
button_7 = tk.Button(gui,text='7',padx=25,pady=15,command = lambda: button_click(7))
button_8 = tk.Button(gui,text='8',padx=25,pady=15,command = lambda: button_click(8))
button_9 = tk.Button(gui,text='9',padx=25,pady=15,command = lambda: button_click(9))

button_add = tk.Button(gui,text='+',padx=25,pady=15,command= button_add)
button_subtract = tk.Button(gui,text='-',padx=25,pady=15, command = button_subtract)
button_multiply = tk.Button(gui,text='*',padx=25,pady=15, command = button_multiply)
button_divide = tk.Button(gui,text='/',padx=25,pady=15, command = button_divide)
button_equal = tk.Button(gui,text='=',padx=25,pady=15,command = button_equal)
button_clear = tk.Button(gui,text='C',padx=25,pady=15,command = button_clear)
#%% place buttons in gui
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)
#%% run main gui
gui.mainloop()











