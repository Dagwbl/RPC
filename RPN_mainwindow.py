#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from sys import exit
import csv
import tkinter as tk
import RPN_function as f
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x300')
window.title('课堂点名')
window.resizable(0,0)

def About_info():
    messagebox.showinfo('About','''还是太菜了，感觉代码写的一塌糊涂，非常感谢袁老师给的锻炼机会，不然一直不会写出一个完整的程序来。\n\
使用说明也不想写啦，毕竟就那么一个功能。此程序已在\nGitHub（https://github.com/Dagwbl/Python_Study.git）\n开源，欢迎fork并告知，学无止境\n 
第一次使用如未配置文件，默认为安全161班学生，单击‘Roll Call’即可开始随机点名。全班学生会在窗口左侧呈现列表，已经被点过名的会在窗口左侧呈现。\n
菜单栏分别对应着\n
配置文件，查询信息，增删信息，关于\n
英语太差，凭直觉理解
哦，对了，千万别打开程序目录的CSV文件，否则会造成程序异常。\
\
早
''')

def name():
    l_top.config(text = 'Click button Start random roll call')
    f.Named()
    list1,list2,counter1,counter2,surplus = f.inquire_ed()
    l_bottom.config(text =  'Surplus: '+str(surplus))
    if flag == False:
        list_al.set(list1)
        list_ed.set(list2[::-1])
        nd_list.place(x=10,y=75,anchor = 'nw')
        all_list.place(x=500,y=75,anchor = 'ne')
        l_top.config(text = list2[-1])
        l_top.pack()



def Uncall_person():
    list1,list2,counter1,counter2,surplus = f.inquire_ed()
    list0 =[]
    for row in list1:
        if row in list2:
            continue
        else:
            list0.append(row)
    str0 = 'All uncalled students are :\n'+str(list0)
    messagebox.showinfo('Uncall list',str0)

def add_student():
    def add_student_to_database():
        Student_id = stu_id.get()
        nn = stu_name.get()
        stu_info = [Student_id,nn]
        list1,list2,counter1,counter2,surplus = f.inquire_ed()
        if stu_info in list1:
            messagebox.showerror('Error', 'The user is already exist!')
        else:
            with open('Students.csv', 'a',encoding = 'utf-8',newline = '') as class_list:
                # pickle.dump(exist_usr_info, class_list)
                writer01 = csv.writer(class_list)
                writer01.writerow(stu_info)
                list1.append(stu_info)
                list_al.set(list1)
                list_ed.set(list2[::-1])
                nd_list.place(x=10,y=75,anchor = 'nw')
                all_list.place(x=500,y=75,anchor = 'ne')
                l_bottom.config(text =  'Surplus: '+str(surplus+1))
                l_bottom.pack(side = 'bottom')
                messagebox.showinfo('Tips', 'Add successfully!')
                add_window.destroy()
    add_window = tk.Toplevel(window)
    add_window.geometry('350x200')
    add_window.title('Add window')

    stu_name = tk.StringVar()
    # stu_name.set('example@python.com')
    tk.Label(add_window, text='Student name: ').place(x=10, y= 50)
    entry_new_name = tk.Entry(add_window, textvariable=stu_name)
    entry_new_name.place(x=150, y=50)

    stu_id = tk.StringVar()
    tk.Label(add_window, text='Student ID: ').place(x=10, y=10)
    entry_usr_pwd = tk.Entry(add_window, textvariable=stu_id, show=None)
    entry_usr_pwd.place(x=150, y=10)
    btn_comfirm_sign_up = tk.Button(add_window, text='Add', command=add_student_to_database)
    btn_comfirm_sign_up.place(x=150, y=130)

def del_studental():
    def del_student_to_database():
        Student_id = stu_id.get()
        nn = stu_name.get()
        stu_info = [Student_id,nn]
        list1,list2,counter1,counter2,surplus = f.inquire_ed()
        if stu_info not in list1:
            messagebox.showerror('Error', "The user isn't exist!")
        else:
            with open('Students.csv', 'w',encoding = 'utf-8',newline = '') as class_list:
                list1.remove(stu_info)
                writer01 = csv.writer(class_list)
                for row in list1:
                    writer01.writerow(row)
                list_al.set(list1)
                list_ed.set(list2[::-1])
                nd_list.place(x=10,y=75,anchor = 'nw')
                all_list.place(x=500,y=75,anchor = 'ne')
                l_bottom.config(text =  'Surplus: '+str(surplus-1))
                l_bottom.pack(side = 'bottom')
                messagebox.showinfo('Tips', 'You have successfully delete!')
                add_window.destroy()
    add_window = tk.Toplevel(window)
    add_window.geometry('350x200')
    add_window.title('Delete window')
    stu_name = tk.StringVar()
    tk.Label(add_window, text='Student name: ').place(x=10, y= 50)
    entry_new_name = tk.Entry(add_window, textvariable=stu_name)
    entry_new_name.place(x=150, y=50)

    stu_id = tk.StringVar()
    tk.Label(add_window, text='Student ID: ').place(x=10, y=10)
    entry_usr_pwd = tk.Entry(add_window, textvariable=stu_id, show=None)
    entry_usr_pwd.place(x=150, y=10)
    btn_comfirm_sign_up = tk.Button(add_window, text='Delete', command=del_student_to_database)
    btn_comfirm_sign_up.place(x=150, y=130)

def add_studented():
    def add_student_to_called():
        Student_id = stu_id.get()
        nn = stu_name.get()
        stu_info = [Student_id,nn]
        list1,list2,counter1,counter2,surplus = f.inquire_ed()
        if stu_info not in list1:
            messagebox.showerror('Error', "The user isn't exist!")
        else:
            with open('Students_ed.csv', 'a',encoding = 'utf-8',newline='') as class_list:
                writer = csv.writer(class_list)
                writer.writerow(stu_info)
                list2.append(stu_info)
                list_al.set(list1)
                list_ed.set(list2[::-1])
                nd_list.place(x=10,y=75,anchor = 'nw')
                all_list.place(x=500,y=75,anchor = 'ne')
                messagebox.showinfo('Tips', 'Add seccessfully!')
                l_bottom.config(text =  'Surplus: '+str(surplus-1))
                l_bottom.pack(side = 'bottom')
                add_window.destroy()
    add_window = tk.Toplevel(window)
    add_window.geometry('350x200')
    add_window.title('Add student to called list')

    stu_name = tk.StringVar()
    tk.Label(add_window, text='Student name: ').place(x=10, y= 50)
    entry_new_name = tk.Entry(add_window, textvariable=stu_name)
    entry_new_name.place(x=150, y=50)

    stu_id = tk.StringVar()
    tk.Label(add_window, text='Student ID: ').place(x=10, y=10)
    entry_usr_pwd = tk.Entry(add_window, textvariable=stu_id, show=None)
    entry_usr_pwd.place(x=150, y=10)
    btn_comfirm_sign_up = tk.Button(add_window, text='Add', command=add_student_to_called)
    btn_comfirm_sign_up.place(x=150, y=130)

def del_student_from_ed():
    def del_student_to_called():
        Student_id = stu_id.get()
        nn = stu_name.get()
        stu_info = [Student_id,nn]
        list1,list2,counter1,counter2,surplus = f.inquire_ed()
        if stu_info not in list2:
            messagebox.showerror('Error', "The user isn't exist!")
            pass
        else:
            list2.remove(stu_info)
            with open('Students_ed.csv', 'w',encoding = 'utf-8',newline='') as class_list:
                writer = csv.writer(class_list)
                for row in list2:
                    writer.writerow(row)
                list_al.set(list1)
                list_ed.set(list2[::-1])
                nd_list.place(x=10,y=75,anchor = 'nw')
                all_list.place(x=500,y=75,anchor = 'ne')
                messagebox.showinfo('Tips', 'Delete seccessfully!')
                l_bottom.config(text =  'Surplus: '+str(surplus+1))
                l_bottom.pack(side = 'bottom')
                add_window.destroy()
    add_window = tk.Toplevel(window)
    add_window.geometry('350x200')
    add_window.title('Delete student from called list')

    stu_name = tk.StringVar()
    tk.Label(add_window, text='Student name: ').place(x=10, y= 50)
    entry_new_name = tk.Entry(add_window, textvariable=stu_name)
    entry_new_name.place(x=150, y=50)

    stu_id = tk.StringVar()
    tk.Label(add_window, text='Student ID: ').place(x=10, y=10)
    entry_usr_pwd = tk.Entry(add_window, textvariable=stu_id, show=None)
    entry_usr_pwd.place(x=150, y=10)
    btn_comfirm_sign_up = tk.Button(add_window, text='Delete', command=del_student_to_called)
    btn_comfirm_sign_up.place(x=150, y=130)

l_top = tk.Label(window, text='', bg='grey',width = 36,height = 2)
l_bottom = tk.Label(window,text = '',width = 12,height = 2)
list_al = tk.StringVar()
list_ed = tk.StringVar()
l_left = tk.Label(window,text = 'Class list')
l_right = tk.Label(window,text = 'Called list')
l_left.place(x=20,y=50,anchor = 'nw')
l_right.place(x=450,y=50,anchor = 'ne')
nd_list = tk.Listbox(window,listvariable = list_al)
all_list = tk.Listbox(window,listvariable = list_ed)

flag = True
if flag:
    # try :
    #     list1,list2,counter1,counter2,surplus = f.inquire_ed()
    # except TypeError:
    #     exit()
        # raise SystemExit
    # print(list1)
    # print(counter1,surplus)
    list1,list2,counter1,counter2,surplus = f.inquire_ed()
    l_top.config(text = 'Surplus ' + str(surplus) + ' students not have  call the roll.')
    l_top.pack()
    l_bottom.config(text =  'Surplus: '+str(surplus))
    l_bottom.pack(side = 'bottom')
    list_al.set(list1)
    list_ed.set(list2[::-1])
    nd_list.place(x=10,y=75,anchor = 'nw')
    all_list.place(x=500,y=75,anchor = 'ne')
    flag = False


menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = 'Open', command = f.chooseFile)
filemenu.add_command(label = 'Reset', command = f.reset_nd)
filemenu.add_separator()
filemenu.add_command(label = 'Exit',command = window.quit)

inquiremenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'Inquire', menu = inquiremenu)
inquiremenu.add_command(label = 'Uncall person',command = Uncall_person)
inquiremenu.add_command(label = 'Students number',command = f.students_num)
inquiremenu.add_command(label = 'Surplus number',command = f.surplus_num)

editmenu = tk.Menu(menubar, tearoff=0)
submenu1 = tk.Menu(editmenu,tearoff = 0)
submenu2 = tk.Menu(editmenu,tearoff = 0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_cascade(label='Add', menu = submenu1, underline = 0)
editmenu.add_cascade(label='Delete', menu = submenu2, underline = 0)
submenu1.add_command(label = 'Add a student to database',command = add_student)
submenu1.add_command(label = 'Add a student to named',command = add_studented)
submenu2.add_command(label = 'Delete a student from database',command = del_studental)
submenu2.add_command(label = 'Delete a student from named',command = del_student_from_ed)

menubar.add_command(label = 'About',command = About_info)




n_button = tk.Button(window,text = 'Roll call',width = 12, \
    height = 5,font = ('Times -17 bold'),command = name)
n_button.place(x =250,y = 150,anchor = 'center')


window.config(menu = menubar)
window.mainloop()
