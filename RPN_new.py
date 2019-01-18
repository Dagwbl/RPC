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
window.resizable(100, 100)
window.configure(bg='#9AC5EA')

l_top = tk.Label(window, text='文字显示区', bg='#22459E',
                fg='#FFFFFF', height=2, font=("Times 17 bold"))
l_top.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)




def About_info():
    messagebox.showinfo('About', '''还是太菜了，感觉代码写的一塌糊涂，非常感谢袁老师给的锻炼机会，不然一直不会写出一个完整的程序来。\n\
    使用说明也不想写啦，毕竟就那么一个功能。此程序已在\nGitHub（https://github.com/Dagwbl/Python_Study.git）\n开源，欢迎fork并告知，学无止境\n 
    第一次使用如未配置文件，默认为安全161班学生，单击‘Roll Call’即可开始随机点名。全班学生会在窗口左侧呈现列表，已经被点过名的会在窗口左侧呈现。\n
    菜单栏分别对应着\n
    配置文件，查询信息，增删信息，关于\n
    英语太差，凭直觉理解
    哦，对了，千万别打开程序目录的CSV文件，否则会造成程序异常。\
    \
    早
    ''')

def score(stu_info):
    def write_score():
        score_ed = score_num.get()
        info = stu_info
        with open(listfile3,'a+',encoding = 'utf-8',newline = '') as lf3:
            writer = csv.writer(lf3)
            writer.writerow([info[0],info[1],str(score_ed)])
            list3.append([info[0],info[1],str(score_ed)])
            list3s.set(list3[::-1])
            score_window.destroy()
    score_window = tk.Toplevel(window)
    score_window.title('请评分')
    score_window.geometry('300x200')
    score_num = tk.IntVar()
    score_num.set(100)
    tk.Label(score_window, text='请输入分数:').grid(column =0,row = 0,rowspan = 2,pady = 40)
    entry_score = tk.Entry(score_window,textvariable = score_num)
    entry_score.grid(row = 0,column = 1,rowspan = 2,pady =40)

    en_button = tk.Button(score_window,text = '确认',command = write_score)
    en_button.grid(row =3,column = 1,sticky= tk.EW)

def yes_or_no(stu_info):
    # stu_id = stu_info[0]
    info = stu_info
    tit = str(info[1]) + '请回答'
    ques = str(info[1]) + " 回答出问题来了吗？"
    sta = messagebox.askyesno(tit,ques)
    if sta:
        score(stu_info)
    else:
        with open(listfile4,'a+',encoding = 'utf-8',newline = '') as lf4:
            writer = csv.writer(lf4)
            reader = csv.reader(lf4)
            writer.writerow(info)
            list4.append(info)
            list4s.set(list4[::-1])
            _list4.pack()
def name():
    l_top.config(text='Click button Start random roll call')
    f.Named()
    list1,list2,list3,list4,counter1,counter2,surplus = f.inquire_ed()
    yes_or_no(list2[-1])
    l_bottom.config(text='Surplus: '+str(surplus))
    # if flag == False:
    list1s.set(list1)
    list2s.set(list2[::-1])
    _list2.pack()
    _list1.pack()
    l_top.config(text=list2[-1])
    l_top.pack()


def Uncall_person():
    list1,list2,list3,list4,counter1,counter2,surplus = f.inquire_ed()
    list0 = []
    for row in list1:
        if row in list2:
            continue
        else:
            list0.append(row)
    str0 = 'All uncalled students are :\n'+str(list0)
    messagebox.showinfo('Uncall list', str0)


def add_student():
    def add_student_to_database():
        Student_id = stu_id.get()
        nn = stu_name.get()
        stu_info = [Student_id, nn]
        list1,list2,list3,list4,counter1,counter2,surplus = f.inquire_ed()
        if stu_info in list1:
            messagebox.showerror('Error', 'The user is already exist!')
        else:
            with open(listfile1, 'a', encoding='utf-8', newline='') as class_list:
                # pickle.dump(exist_usr_info, class_list)
                writer01 = csv.writer(class_list)
                writer01.writerow(stu_info)
                list1.append(stu_info)
                list1s.set(list1)
                list2s.set(list2[::-1])
                _list2.pack()
                _list1.pack()
                l_bottom.config(text='Surplus: '+str(surplus+1))
                l_bottom.pack(side='bottom')
                messagebox.showinfo('Tips', 'Add successfully!')
                add_window.destroy()
    add_window = tk.Toplevel(window)
    add_window.geometry('350x200')
    add_window.title('Add window')

    stu_name = tk.StringVar()
    # stu_name.set('example@python.com')
    tk.Label(add_window, text='Student name: ').place(x=10, y=50)
    entry_new_name = tk.Entry(add_window, textvariable=stu_name)
    entry_new_name.place(x=150, y=50)

    stu_id = tk.StringVar()
    tk.Label(add_window, text='Student ID: ').place(x=10, y=10)
    entry_usr_pwd = tk.Entry(add_window, textvariable=stu_id, show=None)
    entry_usr_pwd.place(x=150, y=10)
    btn_comfirm_sign_up = tk.Button(
        add_window, text='Add', command=add_student_to_database)
    btn_comfirm_sign_up.place(x=150, y=130)

def del_studental():
    def del_student_to_database():
        Student_id = stu_id.get()
        nn = stu_name.get()
        stu_info = [Student_id,nn]
        list1,list2,list3,list4,counter1,counter2,surplus = f.inquire_ed()
        if stu_info not in list1:
            messagebox.showerror('Error', "The user isn't exist!")
        else:
            with open(listfile1, 'w',encoding = 'utf-8',newline = '') as class_list:
                list1.remove(stu_info)
                writer01 = csv.writer(class_list)
                for row in list1:
                    writer01.writerow(row)
                list1s.set(list1)
                list2s.set(list2[::-1])
                _list2.pack()
                _list1.place( )
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
        list1,list2,list3,list4,counter1,counter2,surplus = f.inquire_ed()
        if stu_info not in list1:
            messagebox.showerror('Error', "The user isn't exist!")
        else:
            with open(listfile2, 'a',encoding = 'utf-8',newline='') as class_list:
                writer = csv.writer(class_list)
                writer.writerow(stu_info)
                list2.append(stu_info)
                list1s.set(list1)
                list2s.set(list2[::-1])
                _list2.pack()
                _list1.place( )
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
        list1,list2,list3,list4,counter1,counter2,surplus = f.inquire_ed()
        if stu_info not in list2:
            messagebox.showerror('Error', "The user isn't exist!")
            pass
        else:
            list2.remove(stu_info)
            with open(listfile2, 'w',encoding = 'utf-8',newline='') as class_list:
                writer = csv.writer(class_list)
                for row in list2:
                    writer.writerow(row)
                list1s.set(list1)
                list2s.set(list2[::-1])
                _list2.pack()
                _list1.place( )
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

def print_score():
    list1,list2,list3,list4,counter1,counter2,surplus = f.inquire_ed()
    messagebox.showinfo('成绩',sorted(list3))

listfile1 = 'list1.csv'
listfile2 = 'list2.csv'
listfile3 = 'list3.csv'
listfile4 = 'list4.csv'

page = tk.Frame(window)
page1 = tk.Frame(page)
pagemid = tk.Frame(page)
page2 = tk.Frame(page)

# tk.Label(page1, text="左页", bg="yellow", font=("Arial", 12), width=10, height=2).pack(side='top')
# tk.Label(pagemid, text="", bg="green", font=("Arial", 12), width=10, height=2).pack(side='top')
# tk.Label(page2, text="右页", bg="red", font=("Arial", 12), width=10, height=2).pack(side='top')
pagemid.configure(bg='#9AC5EA')
page1.pack(side='left', expand=tk.YES, fill=tk.Y)
page2.pack(side='right', expand=tk.YES, fill=tk.Y)
pagemid.pack(side='bottom', expand=tk.YES, padx=1, ipady=63)
page.pack(side='top')

tk.Label(pagemid, text="", bg="#9AC5EA", font=(
    "Arial", 12), width=15, height=2).pack(side='top')
n_button = tk.Button(pagemid, text='点名', width=4,
                    height=1, font=('Times 17 bold'), fg='#FFFFFF', bg='#0895A8', padx=12, command=name)
n_button.pack(side='bottom')

tabControl = ttk.Notebook(page1)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='  全部学生  ')
tabControl.add(tab2, text='  已点学生  ')
tabControl.pack(side='top', expand=tk.YES, fill=tk.X)

tabControl2 = ttk.Notebook(page2)
tab3 = ttk.Frame(tabControl2)
tab4 = ttk.Frame(tabControl2)
tabControl2.add(tab3, text='  回答正确  ')
tabControl2.add(tab4, text='  回答错误  ')
tabControl2.pack(side='top', expand=tk.YES, fill=tk.X)

list1s = tk.StringVar()
list2s = tk.StringVar()
# list1.set([1,2,3,4])
# list2.set([1,2])
list1,list2,list3,list4,counter1,counter2,surplus = f.inquire_ed()
list1s.set(list1)
list2s.set(list2)
_list1 = tk.Listbox(tab1, listvariable=list1s)
_list2 = tk.Listbox(tab2, listvariable=list2s)

_list1.pack()
_list2.pack()

list3s = tk.StringVar()
list4s = tk.StringVar()
# list3.set([1,2,3,4])
# list4.set([1,2])
list3s.set(list3[::-1])
list4s.set(list4[::-1])
_list3 = tk.Listbox(tab3, listvariable=list3s)
_list4 = tk.Listbox(tab4, listvariable=list4s)

_list3.pack()
_list4.pack()

l_bottom = tk.Label(window, text='', bg='#71C1ED',
                    fg='#FFFFFF', height=1, font=("Times 12 bold"))
l_bottom.config(text = "剩余未点人数："+ str(surplus))
l_bottom.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.X)

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=f.chooseFile)
filemenu.add_command(label='Reset', command=f.reset_nd)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

printmenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = '打印',menu = printmenu)
printmenu.add_command(label = '打印成绩',command = print_score)

inquiremenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Inquire', menu=inquiremenu)
inquiremenu.add_command(label='Uncall person', command=Uncall_person)
inquiremenu.add_command(label='Students number', command=f.students_num)
inquiremenu.add_command(label='Surplus number', command=f.surplus_num)

editmenu = tk.Menu(menubar, tearoff=0)
submenu1 = tk.Menu(editmenu, tearoff=0)
submenu2 = tk.Menu(editmenu, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_cascade(label='Add', menu=submenu1, underline=0)
editmenu.add_cascade(label='Delete', menu=submenu2, underline=0)
submenu1.add_command(
    label='Add a student to database', command=add_student)
submenu1.add_command(label='Add a student to named', command=add_studented)
submenu2.add_command(
    label='Delete a student from database', command=del_studental)
submenu2.add_command(label='Delete a student from named',
                    command=del_student_from_ed)
menubar.add_command(label='About', command=About_info)
window.config(menu=menubar)

window.mainloop()
