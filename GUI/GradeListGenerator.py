import Tkinter
import sys
from lxml import html
import requests
from Tkinter import *
import math
from collections import *
import os
import tkMessageBox

# copying legacy code over a year back.. sucks 

def getLimit(path):
    cnt = 0
    foo = os.open(path,os.O_RDWR|os.O_CREAT)
    sys.stdin = open(path,'r')
    while True:
        try:
            r = raw_input()
            cnt += 1
        except EOFError:
            sys.stdin.close()
            os.close(foo)
            if cnt == 0:
                app2 = Tkinter.Tk()
                app2.withdraw()
                tkMessageBox.showinfo("Error",'File is empty. Generate List before proceeding')
                return 0
            return cnt
subjects = [['nothing' for i in range(6)]for i in range(9)]

def getSubjectData(path):
    foo = os.open(path,os.O_RDWR|os.O_CREAT)
    sys.stdin = open(path,'r')
    cnt = 0
    while True:
        try:
            r = map(str,raw_input().split())
            for i in range(len(r)):
                subjects[cnt][i] = r[i]
            cnt += 1
        except EOFError:
            sys.stdin.close()
            os.close(foo)
            if cnt == 0:
                app2 = Tkinter.Tk()
                app2.withdraw()
                tkMessageBox.showinfo("Error",'File is empty. Generate List before proceeding')
                return 0
            return cnt

class Redir(object): #redirects stdout to text box

    def __init__(self, text_area):
        self.text_area = text_area

    def write(self, strg):
        self.text_area.insert(END, strg)
        self.text_area.see(END)

class mech: # for mechanical
    n=[""]*200
    r=[""]*200
    s=[""]*200
    g=[""]*200

class elec: # for electrical
    n=[""]*200
    r=[""]*200
    s=[""]*200
    g=[""]*200

class civil:    # for civil
    n=[""]*200
    r=[""]*200
    s=[""]*200
    g=[""]*200

class cse:  # for computer science
    n=[""]*200
    r=[""]*200
    s=[""]*200
    g=[""]*200

class inst:  # for electronics and instrumentation
    n=[""]*200
    r=[""]*200
    s=[""]*200
    g=[""]*200

class biot: # for biotechnology
    n=[""]*200
    r=[""]*200
    s=[""]*200
    g=[""]*200

class tex: # for textile
    n=[""]*200
    r=[""]*200
    s=[""]*200
    g=[""]*200

class it: # for information technology
    n=[""]*200
    r=[""]*200
    s=[""]*200
    g=[""]*200

class ft: # for fashion technology
    n=[""]*200
    r=[""]*200
    s=[""]*200
    g=[""]*200

class barch: # for architecture
    n=[""]*200
    r=[""]*200
    s=[""]*200
    g=[""]*200

def resetList():
    subjects = [['nothing' for i in range(6)]for i in range(9)]
    mech.n = ['']*200
    mech.r = ['']*200
    mech.s = ['']*200
    mech.g = ['']*200

    elec.n = ['']*200
    elec.r = ['']*200
    elec.s = ['']*200
    elec.g = ['']*200

    civil.n = ['']*200
    civil.r = ['']*200
    civil.s = ['']*200
    civil.g = ['']*200

    inst.n = ['']*200
    inst.r = ['']*200
    inst.s = ['']*200
    inst.g = ['']*200

    cse.n = ['']*200
    cse.r = ['']*200
    cse.s = ['']*200
    cse.g = ['']*200

    it.n = ['']*200
    it.r = ['']*200
    it.s = ['']*200
    it.g = ['']*200

    biot.n = ['']*200
    biot.r = ['']*200
    biot.s = ['']*200
    biot.g = ['']*200

    tex.n = ['']*200
    tex.r = ['']*200
    tex.s = ['']*200
    tex.g = ['']*200

    ft.n = ['']*200
    ft.r = ['']*200
    ft.s = ['']*200
    ft.g = ['']*200



# space for adding those branches i missed

ctr=[0]*10   # iterator used in same order as classes
number = 0

def generate(grades,code):
    value = OrderedDict()

    for i in range(6):
        value[i] = OrderedDict([('O',0),('E',0),('A',0),('B',0),('C',0),('D',0),('F',0),('S',0)])
    for i in range(len(grades)):
        ctr = 0
        for j in grades[i]:
            value[ctr][j] += 1
            ctr += 1

    for i in range(6):
        print subjects[code][i]
        print 
        print
        for j in value[i]:
            print '                               '+j+ ': '+str(value[i][j])
        print '            '+'-----------------------------------'

number = -1
def calculateGrade(path):
    ctr=[0]*10
    number = getLimit(path)-1
    foo = os.open(path,os.O_RDWR|os.O_CREAT)
    sys.stdin = open(path,'r')
    if number != -1:
        useless = raw_input()
    for i in range(number): # iterator
        foo = map(str,raw_input().split())
        ff = True
        name = ''
        branch = ''
        grade = ''
        for j in range(len(foo)):
            if 48 <= ord(foo[j][0]) <= 57:
                if ff:
                    roll = foo[j]
                    ff = False
                else:
                    sgpa = foo[j]
            else:
                if ff:
                    name += str(foo[j]) + ' '
                else:
                    if j != len(foo)-1:
                        branch += str(foo[j]) + ' '
                    else:
                        grade += str(foo[j])

        if True:

            if branch=="MECHANICAL ENGINEERING ":
                mech.n[ctr[0]]=name
                mech.s[ctr[0]]=sgpa
                mech.r[ctr[0]]=roll
                mech.g[ctr[0]]=grade
                ctr[0]+=1
            if branch=="ELECTRICAL ENGINEERING ":
                elec.n[ctr[1]]=name
                elec.s[ctr[1]]=sgpa
                elec.r[ctr[1]]=roll
                elec.g[ctr[1]]=grade
                ctr[1]+=1
            if branch=="CIVIL ENGINEERING ":
                civil.n[ctr[2]]=name
                civil.s[ctr[2]]=sgpa
                civil.r[ctr[2]]=roll
                civil.g[ctr[2]]=grade
                ctr[2]+=1
            if branch=="COMPUTER SCIENCE & ENGINEERING ":
                cse.n[ctr[3]]=name
                cse.s[ctr[3]]=sgpa
                cse.r[ctr[3]]=roll
                cse.g[ctr[3]]=grade
                ctr[3]+=1
            if branch=="INSTRUMENTATION & ELECTRONICS ENGINEERING " or branch == "ELECTRONICS AND INSTRUMENTATION ENGINEERING. ":
                inst.n[ctr[4]]=name
                inst.s[ctr[4]]=sgpa
                inst.r[ctr[4]]=roll
                inst.g[ctr[4]]=grade
                ctr[4]+=1
            if branch=="BIO TECHNOLOGY ":
                biot.n[ctr[5]]=name
                biot.s[ctr[5]]=sgpa
                biot.r[ctr[5]]=roll
                biot.g[ctr[5]]=grade
                ctr[5]+=1
            if branch=="TEXTILE ENGINEERING ":
                tex.n[ctr[6]]=name
                tex.s[ctr[6]]=sgpa
                tex.r[ctr[6]]=roll
                tex.g[ctr[6]]=grade
                ctr[6]+=1
            if branch=="INFORMATION TECHNOLOGY ":
                it.n[ctr[7]]=name
                it.s[ctr[7]]=sgpa
                it.r[ctr[7]]=roll
                it.g[ctr[7]]=grade
                ctr[7]+=1
            if branch=="FASHION TECHNOLOGY ":
                ft.n[ctr[8]]=name
                ft.s[ctr[8]]=sgpa
                ft.r[ctr[8]]=roll
                ft.r[ctr[8]]=grade
                ctr[8]+=1
            if branch=="ARCHITECTURE ":
                barch.n[ctr[9]]=name
                barch.s[ctr[9]]=sgpa
                barch.r[ctr[9]]=roll
                barch,g[ctr[9]]=grade


def displayGrade(path):
    app11=Tkinter.Tk()
    number = getLimit(path)-1
    if number == -1:
        app11.withdraw()
    sb=Scrollbar(app11)
    tb=Text(app11,height=36,width=74)
    sb.pack(side=RIGHT,fill=Y)
    tb.pack(side=BOTTOM,fill=Y)
    sb.config(command=tb.yview)
    tb.config(yscrollcommand=sb.set)
    sys.stdout=Redir(tb)
    tb.delete(1.0,END)
    def list_mech():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                       MECHANICAL  ENGINEERING'
        print
        print
        generate(mech.g,0)
        #tb.config(state=DISABLED)

    def list_elec():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                           ELECTRICAL  ENGINEERING'
        print
        print
        generate(elec.g,1)
        #tb.config(state=DISABLED)

    def list_civil():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                               CIVIL  ENGINEERING'
        print
        print
        generate(civil.g,2)
        #tb.config(state=DISABLED)

    def list_ie():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                ELECTRONICS AND INSTRUMENTATION ENGINEERING'
        print
        print
        generate(inst.g,3)
        #tb.config(state=DISABLED)

    def list_cse():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                   COMPUTER SCIENCE AND  ENGINEERING'
        print
        print
        generate(cse.g,4)

        #tb.config(state=DISABLED)
    def list_biot():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                              BIO TECHNOLOGY'
        print
        print
        generate(biot.g,5)
        #tb.config(state=DISABLED)

    def list_it():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                      INFORMATION TECHNOLOGY'
        print
        print
        generate(it.g,6)
        #tb.config(state=DISABLED)

    def list_tex():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                       TEXTILE  ENGINEERING'
        print
        print
        generate(tex.g,7)
        #tb.config(state=DISABLED)

    def list_ft():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                        FASHION TECHNOLOGY'
        print
        print
        generate(ft.g,8)
        #tb.config(state=DISABLED)

    bb0= Menubutton(app11,text="Select Branch",relief=RAISED)
    #bb0.grid()
    bb0.menu=Menu(bb0, tearoff=0)
    bb0["menu"]=bb0.menu
    bb0.menu.add_command(label="Mechanical",command=list_mech)
    bb0.menu.add_command(label="Electrical",command=list_elec)
    bb0.menu.add_command(label="Civil",command=list_civil)
    bb0.menu.add_command(label="Instrumentation",command=list_ie)
    bb0.menu.add_command(label="Computer Science",command=list_cse)
    bb0.menu.add_command(label="Biotechnology",command=list_biot)
    bb0.menu.add_command(label="Information Technology",command=list_it)
    bb0.menu.add_command(label="Textile",command=list_tex)
    bb0.menu.add_command(label="Fashion",command=list_ft)
    bb0.pack()

    app11.title("Grade List")
    app11.mainloop()

