#Anwesh Mohanty

import Tkinter
import sys
from lxml import html
import requests
from Tkinter import *
import math
import tkMessageBox
import os

flag = True

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
            if cnt == 0 or cnt == 1:
                flag = False
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

class elec: # for electrical
    n=[""]*200
    r=[""]*200
    s=[""]*200

class civil:    # for civil
    n=[""]*200
    r=[""]*200
    s=[""]*200

class cse:  # for computer science
    n=[""]*200
    r=[""]*200
    s=[""]*200

class inst:  # for electronics and instrumentation
    n=[""]*200
    r=[""]*200
    s=[""]*200

class biot: # for biotechnology
    n=[""]*200
    r=[""]*200
    s=[""]*200

class tex: # for textile
    n=[""]*200
    r=[""]*200
    s=[""]*200

class it: # for information technology
    n=[""]*200
    r=[""]*200
    s=[""]*200

class ft: # for fashion technology
    n=[""]*200
    r=[""]*200
    s=[""]*200

class barch: # for architecture
    n=[""]*200
    r=[""]*200
    s=[""]*200

def resetList():
    mech.n = ['']*200
    mech.r = ['']*200
    mech.s = ['']*200

    elec.n = ['']*200
    elec.r = ['']*200
    elec.s = ['']*200

    civil.n = ['']*200
    civil.r = ['']*200
    civil.s = ['']*200

    inst.n = ['']*200
    inst.r = ['']*200
    inst.s = ['']*200

    cse.n = ['']*200
    cse.r = ['']*200
    cse.s = ['']*200

    it.n = ['']*200
    it.r = ['']*200
    it.s = ['']*200

    biot.n = ['']*200
    biot.r = ['']*200
    biot.s = ['']*200

    tex.n = ['']*200
    tex.r = ['']*200
    tex.s = ['']*200

    ft.n = ['']*200
    ft.r = ['']*200
    ft.s = ['']*200

    barch.n = ['']*200
    barch.r = ['']*200
    barch.s = ['']*200

# space for adding those branches i missed

ctr=[0]*11   # iterator used in same order as classes

def selsort(a=[]*200,b=[]*200,c=[]*200):
    for i in range(len(c)-1):
        pos=i
        for j in xrange(i,len(c)):
            if c[pos]<c[j]:
                pos=j

        if pos!=i:  # sorts name, roll, sgpa simultaneously, sorted on basis of sgpa
            temp=c[pos]
            c[pos]=c[i]
            c[i]=temp

            temp=b[pos]
            b[pos]=b[i]
            b[i]=temp

            temp=a[pos]
            a[pos]=a[i]
            a[i]=temp

def generate(a=[]*200,b=[]*200,c=[]*200):  # generates rank list
    ctrx=1
    res=c[1]
    for i in range(len(c)):
        q=''
        qq='  '
        
        if c[i]==res and c[i]:
            if ctrx<=9:
                qq+='   '
            elif ctrx>9 and ctrx<99:
                qq+='  '
            else:
                qq+=' '
            print ctrx,qq,a[i],
            for ii in range(25-len(a[i])):
                q+=' '    
            print q,b[i],'    ',c[i] # gives same rank to people with same sgpa
            print ''

        if c[i]!=res and c[i]:
            res=c[i]
            ctrx=i+1
            if ctrx<=9:
                qq+='   '
            elif ctrx>9 and ctrx<99:
                qq+='  '
            else:
                qq+=' '
            print ctrx,qq,a[i],
            for ii in range(25-len(a[i])):
               q+=' '
            print q,b[i],'    ',c[i]
            print ''
number = -1
def calculateRank(path):
    ctr=[0]*10
    resetList()
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
                ctr[0]+=1
            if branch=="ELECTRICAL ENGINEERING ":
                elec.n[ctr[1]]=name
                elec.s[ctr[1]]=sgpa
                elec.r[ctr[1]]=roll
                ctr[1]+=1
            if branch=="CIVIL ENGINEERING ":
                civil.n[ctr[2]]=name
                civil.s[ctr[2]]=sgpa
                civil.r[ctr[2]]=roll
                ctr[2]+=1
            if branch=="COMPUTER SCIENCE & ENGINEERING ":
                cse.n[ctr[3]]=name
                cse.s[ctr[3]]=sgpa
                cse.r[ctr[3]]=roll
                ctr[3]+=1
            if branch=="INSTRUMENTATION & ELECTRONICS ENGINEERING " or branch == "ELECTRONICS AND INSTRUMENTATION ENGINEERING. ":
                inst.n[ctr[4]]=name
                inst.s[ctr[4]]=sgpa
                inst.r[ctr[4]]=roll
                ctr[4]+=1
            if branch=="BIO TECHNOLOGY ":
                biot.n[ctr[5]]=name
                biot.s[ctr[5]]=sgpa
                biot.r[ctr[5]]=roll
                ctr[5]+=1
            if branch=="TEXTILE ENGINEERING ":
                tex.n[ctr[6]]=name
                tex.s[ctr[6]]=sgpa
                tex.r[ctr[6]]=roll
                ctr[6]+=1
            if branch=="INFORMATION TECHNOLOGY ":
                it.n[ctr[7]]=name
                it.s[ctr[7]]=sgpa
                it.r[ctr[7]]=roll
                ctr[7]+=1
            if branch=="FASHION TECHNOLOGY ":
                ft.n[ctr[8]]=name
                ft.s[ctr[8]]=sgpa
                ft.r[ctr[8]]=roll
                ctr[8]+=1
            if branch=="BACHELOR OF ARCHITECTURE ":
                barch.n[ctr[9]]=name
                barch.s[ctr[9]]=sgpa
                barch.r[ctr[9]]=roll
                ctr[9] += 1
def displayRank(path):

    app11=Tkinter.Tk()
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
        print '                          MECHANICAL  ENGINEERING'
        print
        print
        selsort(mech.n,mech.r,mech.s)
        generate(mech.n,mech.r,mech.s)
        #tb.config(state=DISABLED)

    def list_elec():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                            ELECTRICAL  ENGINEERING'
        print
        print
        selsort(elec.n,elec.r,elec.s)
        generate(elec.n,elec.r,elec.s)
        #tb.config(state=DISABLED)

    def list_civil():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                            CIVIL  ENGINEERING'
        print
        print
        selsort(civil.n,civil.r,civil.s)
        generate(civil.n,civil.r,civil.s)
        #tb.config(state=DISABLED)

    def list_ie():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                ELECTRONICS AND INSTRUMENTATION ENGINEERING'
        print
        print
        selsort(inst.n,inst.r,inst.s)
        generate(inst.n,inst.r,inst.s)
        #tb.config(state=DISABLED)

    def list_cse():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                    COMPUTER SCIENCE AND  ENGINEERING'
        print
        print
        selsort(cse.n,cse.r,cse.s)
        generate(cse.n,cse.r,cse.s)

        #tb.config(state=DISABLED)
    def list_biot():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                              BIO TECHNOLOGY'
        print
        print
        selsort(biot.n,biot.r,biot.s)
        generate(biot.n,biot.r,biot.s)
        #tb.config(state=DISABLED)

    def list_it():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                         INFORMATION TECHNOLOGY'
        print
        print
        selsort(it.n,it.r,it.s)
        generate(it.n,it.r,it.s)
        #tb.config(state=DISABLED)

    def list_tex():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                         TEXTILE  ENGINEERING'
        print
        print
        selsort(tex.n,tex.r,tex.s)
        generate(tex.n,tex.r,tex.s)
        #tb.config(state=DISABLED)

    def list_ft():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                          FASHION TECHNOLOGY'
        print
        print
        selsort(ft.n,ft.r,ft.s)
        generate(ft.n,ft.r,ft.s)
        #tb.config(state=DISABLED)

    def list_barch():
        tb.config(state=NORMAL)
        tb.delete(1.0,END)
        print '                                   ARCHITECTURE'
        print
        print
        selsort(barch.n,barch.r,barch.s)
        generate(barch.n,barch.r,barch.s)
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
    bb0.menu.add_command(label="Architecture",command=list_barch)
    bb0.pack()

    app11.title("Rank List")
    app11.mainloop()
