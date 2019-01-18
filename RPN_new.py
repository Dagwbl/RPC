#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from sys import exit
import csv
import tkinter as tk
import RPN_function as f
from tkinter import messagebox, ttk

window = tk.Tk()
window.geometry('500x300')
window.title('课堂点名')
window.resizable(100,100)

def dot():
    pass

l_top = tk.Label(window,text = '文字显示区',bg = 'grey',height = 2,font = ("Times 15 bold"))
l_top.pack(side =tk.TOP,expand = tk.YES,fill=tk.X)

# tabControl = ttk.Notebook(window)
# tab1 = ttk.Frame(tabControl)
# tab2 = ttk.Frame(tabControl)
# tab3 = ttk.Frame(tabControl)
# tab4 = ttk.Frame(tabControl)
# tabControl.add(tab1,text = 'Test1')
# tabControl.add(tab2,text = 'Test2')
# tabControl.add(tab3,text = 'Test3')
# tabControl.add(tab4,text = 'Test4')
# tabControl.grid(column = 0,row = 1,sticky =tk.N)

page = tk.Frame(window)

page1 = tk.Frame(page)
pagemid = tk.Frame(page)
page2 = tk.Frame(page)

# tk.Label(page1, text="左页", bg="yellow", font=("Arial", 12), width=10, height=2).pack(side='top')
# # tk.Label(pagemid, text="占位", bg="green", font=("Arial", 12), width=10, height=2).pack(side='top')
# tk.Label(page2, text="右页", bg="red", font=("Arial", 12), width=10, height=2).pack(side='top')
page1.pack(side = 'left',expand = tk.YES,fill=tk.Y)
page2.pack(side = 'right',expand = tk.YES,fill=tk.Y)
pagemid.pack(side = 'bottom',expand = tk.YES)
page.pack(side = 'top')

n_button = tk.Button(window,text = '点名',width = 5, \
    height = 12,font = ('Times 17 bold'),command = dot)
n_button.pack()


tabControl = ttk.Notebook(page1)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1,text = '     全部     ')
tabControl.add(tab2,text = '     已点     ')
tabControl.pack(side = 'top',expand=tk.YES,fill=tk.X)

tabControl2 = ttk.Notebook(page2)
tab3 = ttk.Frame(tabControl2)
tab4 = ttk.Frame(tabControl2)
tabControl2.add(tab3,text = '     正确     ')
tabControl2.add(tab4,text = '     错误     ')
tabControl2.pack(side = 'top',expand=tk.YES,fill=tk.X)

list1 = tk.StringVar()
list2 = tk.StringVar()
list1.set([1,2,3,4])
list2.set([1,2])
_list1 = tk.Listbox(tab1,listvariable = list1,width = 23)
_list2 = tk.Listbox(tab2,listvariable = list2)
_list1.pack()
_list2.pack()

list3 = tk.StringVar()
list4 = tk.StringVar()
list3.set([1,2,3,4])
list4.set([1,2])
_list3 = tk.Listbox(tab3,listvariable = list3)
_list4 = tk.Listbox(tab4,listvariable = list4)
_list3.pack()
_list4.pack()



window.mainloop()
