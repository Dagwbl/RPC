#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import shutil
import time
import tkinter as tk
from sys import exit
from tkinter import messagebox, ttk
from tkinter.filedialog import askdirectory, asksaveasfilename
from random import randint
import pywintypes
import win32con
from count_time import StopWatch
import os

import RPN_function as f
import win32api

# from pywintypes import 


window = tk.Tk()
window.geometry('500x300')
window.title('课堂提问')
window.resizable(1, 1)
window.configure(bg='#9AC5EA')

l_top = tk.Label(window, text='Less is more', bg='#22459E',
                fg='#FFFFFF', height=2, font=("Times 17 bold"))
l_top.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)


"""  """

def About_info():
    messagebox.showinfo('About', '''\n\
    Nothing is true.\n\
    \n\
    GitHub:\n\
    https://github.com/Dagwbl/RPC.git\n
    
    ''')

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def printfile():
            # defining options for opening a directory  
        dir_opt = options = {}  
        options['initialdir'] = 'D:\\'  
        # options['mustexist'] = False  
        options['parent'] = window  
        options['title'] = '保存至' 
        options['filetypes'] = [("txt文本",'*.txt'),('csv文件','*.csv')]
        
        filename = asksaveasfilename(**dir_opt)
        try :shutil.copy(listfile3,filename)
        except FileNotFoundError:
            messagebox.showinfo('提示','还没有成绩信息')

# def score(stu_info):
#     info = stu_info
#     def WriteFile():
#         score_ed = var1.get()
#         if score_ed:
            # with open(listfile3,'a+',encoding = 'utf-8',newline = '') as lf3:
            #     writer = csv.writer(lf3)
            #     writer.writerow([info[0],info[1],str(score_ed),str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))])
            #     list3.append([info[0],info[1],str(score_ed),str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))])
            #     list3s.set(list3[::-1])
            #     _list3.pack()
#                 # score_window.destroy()
#         else :
#             with open(listfile4,'a+',encoding = 'utf-8',newline = '') as lf4:
#                 writer = csv.writer(lf4)
#                 # reader = csv.reader(lf4)
#                 writer.writerow(info)
#                 list4.append(info)
#                 list4s.set(list4[::-1])
#                 print(list4)
#                 _list4.pack()
    #         score_window.destroy()
    # score_window = tk.Toplevel(window)
    # score_window.title('请评分')
    # score_window.geometry('300x200')
    # score_window.wm_attributes('-topmost',1)
    # score_num = tk.IntVar()
    # score_num.set(100)
    # tk.Label(score_window, text='请输入分数:').grid(column =0,row = 0,rowspan = 2,pady = 40)
    # entry_score = tk.Entry(score_window,textvariable = score_num)
    # entry_score.grid(row = 0,column = 1,rowspan = 2,pady =40)
    # en_button = tk.Button(score_window,text = '确认',command = write_score)
    # en_button.grid(row =3,column = 1,sticky= tk.EW)
    # def callback():
    #     messagebox.showwarning('提示','请输入分数')
    # score_window.protocol("WM_DELETE_WINDOW", callback)


def yes_or_no(stu_info):
    info = stu_info
    def WriteFile():
        if var1.get() == 0:
            with open(listfile4,'a+',encoding = 'utf-8',newline = '') as lf4:
                writer = csv.writer(lf4)
                # reader = csv.reader(lf4)
                writer.writerow(info)
                list4.append(info)
                list4s.set(list4[::-1])
                print(list4)
                _list4.pack()
        else:
            with open(listfile3,'a+',encoding = 'utf-8',newline = '') as lf3:
                writer = csv.writer(lf3)
                writer.writerow([info[0],info[1],str(var1.get()),str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),var2.get()])
                list3.append([info[0],info[1],str(var1.get()),str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),var2.get()])
                list3s.set(list3[::-1])
                _list3.pack()
        AskWindow.destroy()
    def Setlimit():
        swa._limittime = t_limit.get()
        swa.Start()
        # pass
    AskWindow = tk.Toplevel(window)
    AskWindow.title(str(info[1]) + '准备回答')
    # AskWindow.resizable(0,0)
    AskWindow.geometry('280x400')
    # Button0 = tk.Button(AskWindow,text)
    t_label = tk.Label(AskWindow,text = '回答时间限制：')
    t_label.grid(column = 0,row = 1)
    t_limit = tk.IntVar()
    t_limit.set(5)
    t_limit_label = tk.Entry(AskWindow,textvariable = t_limit)
    t_limit_label.grid(column = 0, row = 2)
    swa = StopWatch(AskWindow)
    swa.grid(row = 0,column = 0)
    StButton = tk.Button(AskWindow,text = '开始计时',command = Setlimit)
    StButton.grid(row = 3,column = 0,pady = 6)
    label2 = tk.Label(AskWindow,text = '请输入评分：')
    label2.grid(row = 4,column = 0)
    var1 =tk.IntVar()
    ScoreEntry = tk.Entry(AskWindow,textvariable = var1)
    var1.set(100)
    ScoreEntry.grid(row = 5,column = 0)
    label3 = tk.Label(AskWindow,text = '(提示：0分将加入回答错误列表，供补充提问使用)')
    label3.grid(row = 6,column = 0)
    label4 = tk.Label(AskWindow,text = '备注:')
    label4.grid(row = 7,column = 0,rowspan = 2)
    var2 = tk.StringVar()
    RemarkEntry = tk.Entry(AskWindow,textvariable = var2)
    RemarkEntry.grid(row = 10,column = 0,rowspan = 2)
    CompleteButton = tk.Button(AskWindow,text = '完成',command = WriteFile,font = ('Times 12 bold'))
    CompleteButton.grid(row = 12, column = 0,pady = 12)
    def callback():
        messagebox.showwarning('提示','请给出分数后点击完成退出')
    AskWindow.protocol("WM_DELETE_WINDOW", callback)

    # stu_id = stu_info[0]
    # _,_,_,list4,*_ = f.inquire_ed()
    info = stu_info
    # tit = str(info[1]) + '请回答'
    # ques = str(info[1]) + " 回答出问题来了吗？"
    # sta = messagebox.askyesno(tit,ques)
    # if sta:
    #     sw.Stop()
    #     # sw.Reset()
    #     score(stu_info)

    # else:
    #     sw.Stop()
    # #     # sw.Reset()
    #     with open(listfile4,'a+',encoding = 'utf-8',newline = '') as lf4:
    #         writer = csv.writer(lf4)
    #         # reader = csv.reader(lf4)
    #         writer.writerow(info)
    #         list4.append(info)
    #         list4s.set(list4[::-1])
    #         print(list4)
    #         _list4.pack()

def name():
    # window.after(0,delaytime)
    # # window.after(3000,f.Named)
    # time.sleep(3)
    list1,list2,_,list4,*_,surplus = f.inquire_ed()
    if surplus ==0 and len(list4)!=0:
        messagebox.showinfo('提示','所有学生已经点完，且尚有回答错误的同学，请开始第二轮提问，将从回答错误的列表中抽取。如需强制忽略，可从菜单》文件》重置即可')
    elif surplus ==0 and len(list4)==0:
        messagebox.showinfo('提示','所有学生已经点完，请备份好数据并重置')
    else:
        f.Named()
        list1,list2,_,list4,*_,surplus = f.inquire_ed()
        l_top.config(text=list2[-1])
        yes_or_no(list2[-1])
        
        l_bottom.config(text='Surplus: '+str(surplus))
        # if flag == False:
        list1s.set(list1)
        list2s.set(list2[::-1])
        _list2.pack()
        _list1.pack()
        # l_top.config(text=list2[-1])
        l_top.pack()
def name2():
    _,_,list3,list4,*_ = f.inquire_ed()
    # print(counter1,counter2,surplus)
    # print(list2)
    if len(list4) == 0:
        messagebox.showinfo('Tips','尚未没有回答错误的学生，请先开始第一轮提问！')
        # if bool_1 == True:
        #     reset_nd()
        # else:
        #     pass
    else:
        flag = True
        while flag:
            limite = len(list4)-1
            lucky = randint(0,limite)
            lucky_person = list4[lucky]
            # print(lucky)
            # print(lucky_person)
            ids = [row[0] for row in list3]
            if  lucky_person[0] not in ids:
                list4.remove(lucky_person)
                flag = False
                os.remove(listfile4)
                with open(listfile4,'w',encoding = 'utf-8',newline ='') as lf4:
                    writer = csv.writer(lf4)
                    writer.writerows(list4)
                # list1,list2,list3,list4,counter1,counter2,surplus = f.inquire_ed()
                list4s.set(list4[::-1])
                _list4.pack()
                l_top.config(text=lucky_person)
                yes_or_no(lucky_person)
                flag = False
            else:
                continue

def Uncall_person():
    list1,list2,*_ = f.inquire_ed()
    list0 = []
    for row in list1:
        if row in list2:
            continue
        else:
            list0.append(row)
    str0 = '还没有被点到的人 :\n'+str(list0)
    messagebox.showinfo('Uncall list', str0)

def add_student():
    def add_student_to_database():
        Student_id = stu_id.get()
        nn = stu_name.get()
        stu_info = [Student_id, nn]
        list1,list2,*_,surplus = f.inquire_ed()
        if stu_info in list1:
            messagebox.showerror('Error', '学生信息已存在!')
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
                # messagebox.showinfo('Tips', 'Add successfully!')
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
        list1,list2,*_,surplus = f.inquire_ed()
        if stu_info not in list1:
            messagebox.showerror('Error', "学生信息不存在!")
        else:
            with open(listfile1, 'w',encoding = 'utf-8',newline = '') as lf1:
                list1.remove(stu_info)
                writer01 = csv.writer(lf1)
                for row in list1:
                    writer01.writerow(row)
                list1s.set(list1)
                list2s.set(list2[::-1])
                _list2.pack()
                _list1.place( )
                l_bottom.config(text =  'Surplus: '+str(surplus-1))
                l_bottom.pack(side = 'bottom')
                messagebox.showinfo('Tips', '已成功删除!')
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
        list1,list2,*_,surplus = f.inquire_ed()
        if stu_info not in list1:
            messagebox.showerror('Error', "学生信息不存在!")
        else:
            with open(listfile2, 'a',encoding = 'utf-8',newline='') as class_list:
                writer = csv.writer(class_list)
                writer.writerow(stu_info)
                list2.append(stu_info)
                # list1s.set(list1)
                list2s.set(list2[::-1])
                _list2.pack()
                # _list1.place( )
                yes_or_no(stu_info)
                # messagebox.showinfo('Tips', 'Add seccessfully!')
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

def del_score(stu_info):
        # score_ed = score_num.get()
        info = stu_info
        if info in list4:
            list4.remove(info)
            # os.remove(listfile4)
            with open(listfile4,'w+',encoding = 'utf-8',newline='')as lf4:
                writer = csv.writer(lf4)
                writer.writerows(list4)
                list4s.set(list4)
                _list4.pack()
        else :
            with open(listfile3,'r',encoding = 'utf-8',newline = '') as lf3:
                # writer = csv.writer(lf3)
                reader = csv.reader(lf3)
                list0 =[]
                for row in reader:
                    if info[0] !=row[0]:
                        list0.append(row)
                    else : pass
            os.remove(listfile3)
            with open(listfile3,'w',encoding = 'utf-8',newline = '') as lf3:
                writer = csv.writer(lf3)
                # for row in list0:
                writer.writerows(list0)
            list3s.set(list0[::-1])
            _list3.pack()


def del_student_from_ed():
    def del_student_to_called():
        Student_id = stu_id.get()
        nn = stu_name.get()
        stu_info = [Student_id,nn]
        _,list2,*_,surplus = f.inquire_ed()
        if stu_info  in list2:
            list2.remove(stu_info)
            os.remove(listfile2)
            with open(listfile2, 'w',encoding = 'utf-8',newline='') as lf2:
                writer = csv.writer(lf2)
                # for row in list2:
                writer.writerows(list2)
                # list1s.set(list1)
                list2s.set(list2[::-1])
                _list2.pack()
                # _list1.place()
            del_score(stu_info)
            messagebox.showinfo('Tips', '删除成功!')
            l_bottom.config(text =  'Surplus: '+str(surplus+1))
            l_bottom.pack(side = 'bottom')
            add_window.destroy()
        else :
            messagebox.showerror('Error', "学生信息不存在!")
            

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
    _,_,list3,*_ = f.inquire_ed()
    messagebox.showinfo('成绩',sorted(list3))

listfile1 = 'list1.csv'
listfile2 = 'list2.csv'
listfile3 = 'list3.csv'
listfile4 = 'list4.csv'

page = tk.Frame(window)
page1 = tk.Frame(page)
pagemid = tk.Frame(page)
page2 = tk.Frame(page)

pagemid.configure(bg='#9AC5EA')
page1.pack(side='left', expand=tk.YES, fill=tk.Y)
page2.pack(side='right', expand=tk.YES, fill=tk.Y)
pagemid.pack(side='bottom', expand=tk.YES, padx=1,fill = tk.Y)
page.pack(side='top')

pagemid1 = tk.Frame(pagemid)
pagemid1.pack()
pagemid2 =tk.Frame(pagemid,bg="#9AC5EA")
pagemid2.pack()
sw = StopWatch(pagemid1)
sw.pack(side = 'top')
tk.Button(pagemid1,text='Start',command=sw.Start).pack(side=tk.LEFT,anchor = 'nw',pady = 0)
tk.Button(pagemid1,text='Stop',command=sw.Stop).pack(side=tk.LEFT,anchor = 'n',pady = 0)
tk.Button(pagemid1,text='Reset',command=sw.Reset).pack(side=tk.LEFT,anchor = 'ne',pady =0)
# tk.Button(pagemid,text='Quit',command=sw.quit).pack(side=tk.LEFT)

tk.Label(pagemid2, text="", bg="#9AC5EA", font=(
    "Arial", 12),height = 3).pack(side='top')
n_button = tk.Button(pagemid2, text='提问', width=4,
                    height=1, font=('Times 17 bold'), fg='#FFFFFF', bg='#0895A8', padx=12, command=combine_funcs(name))
n2_button = tk.Button(pagemid2, text='补充提问', width=6,
height=1, font=('Times 11 normal'), fg='#FFFFFF', bg='#6c8cd5', command=combine_funcs(name2))
n2_button.pack(side = tk.BOTTOM,fill = tk.X,pady = 6,anchor = 'n')
n_button.pack(side=tk.BOTTOM,fill = tk.X,pady = 6)

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
list2s.set(list2[::-1])
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
l_bottom.config(text = "surplus："+ str(surplus))
l_bottom.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.X)
# def modifiy(n):
#     # CommandString = 'start notepad list' + str(n) +'.csv' 
#     fileName = 'list' + str(n) + '.csv'
#     win32api.ShellExecute(0, 'open', 'notepad.exe', fileName,'',1)
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
# submenu = tk.Menu(filemenu,tearoff=0)
menubar.add_cascade(label='文件', menu=filemenu)
filemenu.add_command(label='打开', command=f.chooseFile)
filemenu.add_command(label='重置', command=f.reset_nd)
# filemenu.add_cascade(label = '修改',menu = submenu)
# submenu.add_command(label = '全部学生',command= modifiy(1))
# submenu.add_command(label = '已点学生',command= modifiy(2))
# submenu.add_command(label = '回答正确',command= modifiy(3))
# submenu.add_command(label = '回答错误',command= modifiy(4))
filemenu.add_separator()
filemenu.add_command(label='退出', command=window.quit)

printmenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = '打印',menu = printmenu)
printmenu.add_command(label = '打印成绩',command = print_score)
printmenu.add_command(label = '打印到文件',command = printfile)
inquiremenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='查询', menu=inquiremenu)
inquiremenu.add_command(label='未点名单', command=Uncall_person)
inquiremenu.add_command(label='班级人数', command=f.students_num)
inquiremenu.add_command(label='剩余人数', command=f.surplus_num)

editmenu = tk.Menu(menubar, tearoff=0)
submenu1 = tk.Menu(editmenu, tearoff=0)
submenu2 = tk.Menu(editmenu, tearoff=0)
menubar.add_cascade(label='编辑', menu=editmenu)
editmenu.add_cascade(label='添加', menu=submenu1, underline=0)
editmenu.add_cascade(label='删除', menu=submenu2, underline=0)
submenu1.add_command(
    label='添加到班级列表', command=add_student)
submenu1.add_command(label='添加到已点列表', command=add_studented)
submenu2.add_command(
    label='从班级中删除', command=del_studental)
submenu2.add_command(label='从已点列表删除',
                    command=del_student_from_ed)
menubar.add_command(label='关于', command=About_info)
window.config(menu=menubar)

win32api.SetFileAttributes(listfile1,win32con.FILE_ATTRIBUTE_HIDDEN)
try :
    win32api.SetFileAttributes(listfile2,win32con.FILE_ATTRIBUTE_HIDDEN)
except pywintypes.error :
    pass
try:
    win32api.SetFileAttributes(listfile3,win32con.FILE_ATTRIBUTE_HIDDEN)
except pywintypes.error:pass
try:
    win32api.SetFileAttributes(listfile4,win32con.FILE_ATTRIBUTE_HIDDEN)
except pywintypes.error :
    pass

window.mainloop()
