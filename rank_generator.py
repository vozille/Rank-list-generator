#Anwesh Mohanty
#Python 2.7.9

import Tkinter
import sys
from lxml import html
import requests
from Tkinter import *
import math

app=Tkinter.Tk()
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

# space for adding those branches i missed

ctr=[0]*10   # iterator used in same order as classes

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

for i in xrange(1301106000,1301106608): # iterator

    page=requests.get("http://results.bput.ac.in/398_RES/%s.html"%str(i)) # address

    #change the value of the address and the iterator to get the desired results

    tree=html.fromstring(page.text)

    name=tree.xpath("/html/body/table/tr[3]/td/table/tr[2]/td[2]/b/text()")
    branch=tree.xpath("/html/body/table/tr[3]/td/table/tr[4]/td[2]/b/text()")
    roll=tree.xpath("/html/body/table/tr[3]/td/table/tr[1]/td[2]/text()")
    sgpa=tree.xpath("/html/body/table/tr[5]/td/table/tr[13]/td[3]/text()")

    if name and sgpa:   # by checking for both name and sgpa, we can be sure to filter all empty nodes

        print name[0],' ',roll[0],' ',branch[0],' ',sgpa[0] #check progress
        print ''

        if branch[0]=="MECHANICAL ENGINEERING":
            mech.n[ctr[0]]=name[0]
            mech.s[ctr[0]]=sgpa[0]
            mech.r[ctr[0]]=roll[0]
            ctr[0]+=1
        if branch[0]=="ELECTRICAL ENGINEERING":
            elec.n[ctr[1]]=name[0]
            elec.s[ctr[1]]=sgpa[0]
            elec.r[ctr[1]]=roll[0]
            ctr[1]+=1
        if branch[0]=="CIVIL ENGINEERING":
            civil.n[ctr[2]]=name[0]
            civil.s[ctr[2]]=sgpa[0]
            civil.r[ctr[2]]=roll[0]
            ctr[2]+=1
        if branch[0]=="COMPUTER SCIENCE & ENGINEERING":
            cse.n[ctr[3]]=name[0]
            cse.s[ctr[3]]=sgpa[0]
            cse.r[ctr[3]]=roll[0]
            ctr[3]+=1
        if branch[0]=="INSTRUMENTATION & ELECTRONICS ENGINEERING":
            inst.n[ctr[4]]=name[0]
            inst.s[ctr[4]]=sgpa[0]
            inst.r[ctr[4]]=roll[0]
            ctr[4]+=1
        if branch[0]=="BIOTECHNOLOGY":
            biot.n[ctr[5]]=name[0]
            biot.s[ctr[5]]=sgpa[0]
            biot.r[ctr[5]]=roll[0]
            ctr[5]+=1
        if branch[0]=="TEXTILE ENGINEERING":
            tex.n[ctr[6]]=name[0]
            tex.s[ctr[6]]=sgpa[0]
            tex.r[ctr[6]]=roll[0]
            ctr[6]+=1
        if branch[0]=="INFORMATION TECHNOLOGY":
            it.n[ctr[7]]=name[0]
            it.s[ctr[7]]=sgpa[0]
            it.r[ctr[7]]=roll[0]
            ctr[7]+=1
        if branch[0]=="FASHION & APPAREL TECHNOLOGY":
            ft.n[ctr[8]]=name[0]
            ft.s[ctr[8]]=sgpa[0]
            ft.r[ctr[8]]=roll[0]
            ctr[8]+=1
        if branch[0]=="ARCHITECTURE":
            barch.n[ctr[9]]=name[0]
            barch.s[ctr[9]]=sgpa[0]
            barch.r[ctr[9]]=roll[0]

sb=Scrollbar(app)
tb=Text(app,height=36,width=74)
sb.pack(side=RIGHT,fill=Y)
tb.pack(side=BOTTOM,fill=Y)
sb.config(command=tb.yview)
tb.config(yscrollcommand=sb.set)
sys.stdout=Redir(tb)

def list_mech():
    tb.config(state=NORMAL)
    tb.delete(1.0,END)
    selsort(mech.n,mech.r,mech.s)
    generate(mech.n,mech.r,mech.s)
    tb.config(state=DISABLED)
def list_elec():
    tb.config(state=NORMAL)
    tb.delete(1.0,END)
    selsort(elec.n,elec.r,elec.s)
    generate(elec.n,elec.r,elec.s)
    tb.config(state=DISABLED)
def list_civil():
    tb.config(state=NORMAL)
    tb.delete(1.0,END)
    selsort(civil.n,civil.r,civil.s)
    generate(civil.n,civil.r,civil.s)
    tb.config(state=DISABLED)
def list_ie():
    tb.config(state=NORMAL)
    tb.delete(1.0,END)
    selsort(inst.n,inst.r,inst.s)
    generate(inst.n,inst.r,inst.s)
    tb.config(state=DISABLED)
def list_cse():
    tb.config(state=NORMAL)
    tb.delete(1.0,END)
    selsort(cse.n,cse.r,cse.s)
    generate(cse.n,cse.r,cse.s)
    tb.config(state=DISABLED)
def list_biot():
    tb.config(state=NORMAL)
    tb.delete(1.0,END)
    selsort(biot.n,biot.r,biot.s)
    generate(biot.n,biot.r,biot.s)
    tb.config(state=DISABLED)
def list_it():
    tb.config(state=NORMAL)
    tb.delete(1.0,END)
    selsort(it.n,it.r,it.s)
    generate(it.n,it.r,it.s)
    tb.config(state=DISABLED)
def list_tex():
    tb.config(state=NORMAL)
    tb.delete(1.0,END)
    selsort(tex.n,tex.r,tex.s)
    generate(tex.n,tex.r,tex.s)
    tb.config(state=DISABLED)
def list_ft():
    tb.config(state=NORMAL)
    tb.delete(1.0,END)
    selsort(ft.n,ft.r,ft.s)
    generate(ft.n,ft.r,ft.s)
    tb.config(state=DISABLED)

bb0= Menubutton(app,text="Select Branch",relief=RAISED)
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

app.title("Rank Generator By Anwesh Mohanty")
app.mainloop()
