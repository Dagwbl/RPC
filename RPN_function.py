#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import os
import random
import shutil
import time
from tkinter import messagebox,filedialog

from Source import Source

listfile1 = 'list1.csv'
listfile2 = 'list2.csv'
listfile3 = 'list3.csv'
listfile4 = 'list4.csv'

def reset_nd():
    jud = messagebox.askyesno('Warning','将删除所有相关记录文件， 此操作不可逆，是否继续？')
    if jud:
        os.remove(listfile2)
        try:os.remove(listfile3)
        except FileNotFoundError:pass
        try:os.remove(listfile4)
        except FileNotFoundError:pass
        messagebox.showinfo('Tips','删除成功，请关闭程序并重新启动.')
    else:
        pass

def inquire_ed():
    counter1 = 0
    counter2 = 0
    surplus = 0
    list1 =[]
    list2 = []
    list4 = []
    list3 = []
    try:
        with open(listfile4,'r',encoding = 'utf-8',newline = '') as lf4:
            # writer = csv.writer(lf4)
            reader = csv.reader(lf4)
            # writer.writerow([info[0],info[1],str(score_ed)])
            for row in reader:
                list4.append(row)
            # list4s.set(list4)
    except FileNotFoundError:
        pass
    try:
        with open(listfile3,'r',encoding = 'utf-8',newline = '') as lf3:
            # writer = csv.writer(lf4)
            reader = csv.reader(lf3)
            # writer.writerow([info[0],info[1],str(score_ed)])
            for row in reader:
                list3.append(row)
            # list3s.set(list3)
    except FileNotFoundError:
        pass
    try:
        with open(listfile1,'r',newline = '',encoding = 'utf-8') as students:
            reader = csv.reader(students)
            for j in reader:
                if j:
                    counter1+=1
                    list1.append(j)
    except FileNotFoundError:
        mes = messagebox.askquestion('Tips','未发现本地配置文件\n是否使用默认数据 (安全工程161班)\n \
点击“否”可选择数据文件.(csv格式) \n \
例如  \n\n\
1600000,沸羊羊  \n\
1600001,喜羊羊  \n\
1600002,美羊羊')
        if mes =='yes':
            counter1 = 0
            try:
                os.rename(listfile2,'.list2.bak')
            except FileExistsError:
                os.remove('.list2.bak')
                os.rename(listfile2,'.list2.bak')
            except FileNotFoundError:
                pass
            with open(listfile1,'w',newline = '',encoding = 'utf-8') as students:
                writer = csv.writer(students)
                list1,counter1= Source()[::]
                for j in list1:
                    # print(j)
                    if j:
                        writer.writerow(j)
                else :
                    pass
        else :
            chooseFile()
    except UnicodeDecodeError:
        counter1 = 0
        with open(listfile1,'r',newline = '') as students:
            reader = csv.reader(students)
            try:
                for j in reader:
                    if j:
                        counter1+=1
                        list1.append(j)
            except UnicodeDecodeError:
                messagebox.showerror('Error','A serious error was encountered, possibly due to corrupted data files.')
    try:
        with open(listfile2,'r',encoding = 'utf-8') as students_ed:
            reader_ed = csv.reader(students_ed)
            for y in reader_ed:
                if y:
                    counter2+=1
                    list2.append(y)
    except NameError:
        with open(listfile2,'r') as students_ed:
            reader_ed = csv.reader(students_ed)
            for y in reader_ed:
                if y:
                    counter2+=1
                    list2.append(y)
    except FileNotFoundError:
        with open(listfile2,'w+',encoding = 'utf-8',newline='') as students_ed:
            reader_ed = csv.reader(students_ed)
            for y in reader_ed:
                if y:
                    counter2+=1
                    list2.append(y)
        pass
    surplus = counter1-counter2
    return list1,list2,list3,list4,counter1,counter2,surplus

def chooseFile():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    if filename != '':
        # lb.config(text = 'The file you choose is '+ filename)
        surefile = messagebox.askyesno('Tips','确定选择此文件吗？将覆盖之前的所有数据')
        if surefile == True:
            try:
                os.rename(listfile1,'.list1.bak')
                shutil.copy(filename,listfile1)
            except FileExistsError:
                os.remove('.list1.bak')
                shutil.copy(filename,listfile1)
            except FileNotFoundError:
                shutil.copy(filename,listfile1)
            try:os.remove(listfile2)
            except FileNotFoundError:pass
            try:os.remove(listfile3)
            except FileNotFoundError:pass
            try:os.remove(listfile4)
            except FileNotFoundError:pass
            messagebox.showinfo('提示','数据配置完成，请关闭程序并重新启动！') 
            return True
    else :
        return False


def students_num():
    list1,list2,list3,list4,counter1,counter2,surplus = inquire_ed()
    str0 = 'There are '+str(counter1)+' students in this class.'
    messagebox.showinfo('Students number',str0)

def surplus_num():
    list1,list2,list3,list4,counter1,counter2,surplus = inquire_ed()
    messagebox.showinfo('Surplus number',str(surplus))

def Named():
    list1,list2,list3,list4,counter1,counter2,surplus = inquire_ed()
    print(counter1,counter2,surplus)
    # print(list2)
    if surplus == 0 and len(list4) == 0:
        bool_1 = messagebox.askyesno('Tips','所有人都已经被点过，点击“是”将删除记录并重新开始，请确认相关数据是否已备份。')
        if bool_1 == True:
            reset_nd()
        else:
            pass
    else:
        flag = True
        while flag:
            lucky = random.randint(0,counter1-1)
            lucky_person = list1[lucky]
            print(lucky)
            print(lucky_person)
            if  lucky_person not in list2:
                with open(listfile2,'a',encoding = 'utf-8',newline = '') as pointed:
                    writer = csv.writer(pointed)
                    writer.writerow(lucky_person)
                    list2.append(lucky_person)
                    flag = False

def replacefile(filename):
    filename = filename
    shutil.move(listfile1,'list1_old.csv')
    shutil.move(listfile2,'list2_old.csv')
    shutil.copy(filename,listfile1)
    messagebox.showinfo('提示','替换完成，请关闭程序并重新启动！')
