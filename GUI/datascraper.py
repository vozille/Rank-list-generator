#Anwesh Mohanty

import Tkinter
import sys
from lxml import html
import requests
from Tkinter import *
import math
import tkMessageBox
import os
# import rank_generator
# import rankGenUI

number = 0
ind = ["MECHANICAL ENGINEERING ","ELECTRICAL ENGINEERING ","CIVIL ENGINEERING ","INSTRUMENTATION & ELECTRONICS ENGINEERING "\
,"COMPUTER SCIENCE & ENGINEERING ","BIO TECHNOLOGY ","INFORMATION TECHNOLOGY ","TEXTILE ENGINEERING ","FASHION TECHNOLOGY "]
visited = [False]*len(ind)

subjects = [['nothing' for i in range(6)]for i in range(len(ind))]

def formatting(a,b,c,d,e):
    ans = a + ' '*(30 - len(a)) + b + ' '*5 + c + ' '*(45 - len(c)) + d+'          '+e
    return ans

def show(n,a,path): # iterator, address
    try:
        f = os.open(path,os.O_WRONLY|os.O_APPEND|os.O_CREAT)
        sys.stdout = open(path,'a')
        i = n
        add = a
        webAddress = "http://results.bput.ac.in/"+str(add)+"_RES/"
        page=requests.get(webAddress+"%s.html"%str(i))

        tree=html.fromstring(page.text)

        name=tree.xpath("/html/body/table/tr[3]/td/table/tr[2]/td[2]/b/text()")
        branch=tree.xpath("/html/body/table/tr[3]/td/table/tr[4]/td[2]/b/text()")
        roll=tree.xpath("/html/body/table/tr[3]/td/table/tr[1]/td[2]/text()")
        sgpa = [0]
        if len(name) != 0:
            count = tree.xpath("/html/body/table/tr[5]/td/table/tr[position() > 1]/td[1]/text()")
            del count[-1]
            count = map(int,count)
            sgpa = []
            sgpa=tree.xpath("/html/body/table/tr[5]/td/table/tr[%s]/td[3]/text()"%str(max(count)+2))

        if name and sgpa:
            if branch[0] == "ELECTRONICS AND INSTRUMENTATION ENGINEERING. ":
                branch[0] = "INSTRUMENTATION & ELECTRONICS ENGINEERING "


        grades = tree.xpath("/html/body/table/tr[5]/td/table/tr[position() > 1 and position() < 8]/td[5]/text()")
        sub = tree.xpath("/html/body/table/tr[5]/td/table/tr[position() > 1 and position() < 8]/td[3]/text()")
        grades = ''.join(grades)

        if name and sgpa:
            res = ind.index(branch[0]+' ')
            if not visited[res]:
                visited[res] = True
                for x in range(6):
                    subjects[res][x] = sub[x]


       
        if name and sgpa:
            print name[0],roll[0],branch[0],sgpa[0],grades
            sys.stdout.close()
            os.close(f)
            ans = formatting(name[0],roll[0],branch[0],sgpa[0],grades)
            return ans
        else:
            return '0'
    except requests.ConnectionError:
        app2 = Tkinter.Tk()
        app2.withdraw()
        tkMessageBox.showinfo("Error",'No Internet Connection')
        return '-1'

def getSubject(path):
    f = os.open(path,os.O_WRONLY|os.O_APPEND|os.O_CREAT)
    sys.stdout = open(path,'w')
    for i in subjects:
        for j in i:
            j = j.replace(' ','-')
            print j,
        print
    sys.stdout.close()
    os.close(f)
