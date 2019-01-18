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
    jud = messagebox.askyesno('Warning','Are you sure reset named file? This operation is irreversible.')
    if jud:
        os.remove(listfile2)
        messagebox.showinfo('Tips','The file has been reset, now you can begin a new lap.')
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
        mes = messagebox.askquestion('Tips','No data files were found\nWhether to use default data (Safety Engineering 161)\n \
click No to set base data.(*csvfile) \n \
example  \n\
123456,李红  \n\
456789,李明')
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
                    print(j)
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
        surefile = messagebox.askyesno('Tips','Are you sure select this file replace the current one? This operation is irreversible.')
        if surefile == True:
            try:
                os.rename(listfile1,'.list1.bak')
                shutil.copy(filename,listfile1)
            except FileExistsError:
                os.remove('.list1.bak')
                shutil.copy(filename,listfile1)
            except FileNotFoundError:
                shutil.copy(filename,listfile1)
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
    if surplus == 0:
        bool_1 = messagebox.askyesno('Tips','Everyone has been called.\nDo you want to reset data?(y/n)')
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
