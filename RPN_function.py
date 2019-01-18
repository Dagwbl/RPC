#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import os
import random
import shutil
import time
from tkinter import messagebox,filedialog

from Source import Source

Studentsfile = 'Students.csv'
Students_edfile = 'Students_ed.csv'

def reset_nd():
    jud = messagebox.askyesno('Warning','Are you sure reset named file? This operation is irreversible.')
    if jud:
        os.remove(Students_edfile)
        messagebox.showinfo('Tips','The file has been reset, now you can begin a new lap.')
    else:
        pass

def inquire_ed():
    counter1 = 0
    counter2 = 0
    surplus = 0
    list1 =[]
    list2 = []
    try:
        with open(Studentsfile,'r',newline = '',encoding = 'utf-8') as students:
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
                os.rename(Students_edfile,'Studented_old.bak')
            except FileExistsError:
                os.remove('Studented_old.bak')
                os.rename(Students_edfile,'Studented_old.bak')
            except FileNotFoundError:
                pass
            with open(Studentsfile,'w',newline = '',encoding = 'utf-8') as students:
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
        with open(Studentsfile,'r',newline = '') as students:
            reader = csv.reader(students)
            try:
                for j in reader:
                    if j:
                        counter1+=1
                        list1.append(j)
            except UnicodeDecodeError:
                messagebox.showerror('Error','A serious error was encountered, possibly due to corrupted data files.')
    try:
        with open(Students_edfile,'r',encoding = 'utf-8') as students_ed:
            reader_ed = csv.reader(students_ed)
            for y in reader_ed:
                if y:
                    counter2+=1
                    list2.append(y)
    except NameError:
        with open(Students_edfile,'r') as students_ed:
            reader_ed = csv.reader(students_ed)
            for y in reader_ed:
                if y:
                    counter2+=1
                    list2.append(y)
    except FileNotFoundError:
        with open(Students_edfile,'w+',encoding = 'utf-8',newline='') as students_ed:
            reader_ed = csv.reader(students_ed)
            for y in reader_ed:
                if y:
                    counter2+=1
                    list2.append(y)
        pass
    surplus = counter1-counter2
    return list1,list2,counter1,counter2,surplus

def chooseFile():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    if filename != '':
        # lb.config(text = 'The file you choose is '+ filename)
        surefile = messagebox.askyesno('Tips','Are you sure select this file replace the current one? This operation is irreversible.')
        if surefile == True:
            try:
                os.rename(Studentsfile,'Studentsfile.bak')
                shutil.copy(filename,Studentsfile)
            except FileExistsError:
                os.remove('Studentsfile.bak')
                shutil.copy(filename,Studentsfile)
            except FileNotFoundError:
                shutil.copy(filename,Studentsfile)
            return True
    else :
        return False


def students_num():
    list1,list2,counter1,counter2,surplus = inquire_ed()
    str0 = 'There are '+str(counter1)+' students in this class.'
    messagebox.showinfo('Students number',str0)

def surplus_num():
    list1,list2,counter1,counter2,surplus = inquire_ed()
    messagebox.showinfo('Surplus number',str(surplus))

def Named():
    list1,list2,counter1,counter2,surplus = inquire_ed()
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
                with open(Students_edfile,'a',encoding = 'utf-8',newline = '') as pointed:
                    writer = csv.writer(pointed)
                    writer.writerow(lucky_person)
                    list2.append(lucky_person)
                    flag = False

def replacefile(filename):
    filename = filename
    shutil.move(Studentsfile,'Students_old.csv')
    shutil.move(Students_edfile,'Students_ed_old.csv')
    shutil.copy(filename,Studentsfile)
