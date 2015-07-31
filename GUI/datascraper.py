#Anwesh Mohanty

import Tkinter
import sys
from lxml import html
import requests
from Tkinter import *
import math
import tkMessageBox
import os
import time
# import rank_generator
# import rankGenUI

number = 0
ind = ["MECHANICAL ENGINEERING ","ELECTRICAL ENGINEERING ","CIVIL ENGINEERING ","INSTRUMENTATION & ELECTRONICS ENGINEERING "\
,"COMPUTER SCIENCE & ENGINEERING ","BIO TECHNOLOGY ","INFORMATION TECHNOLOGY ","TEXTILE ENGINEERING ","FASHION TECHNOLOGY "]
visited = [False]*len(ind)

subjects = [[]for i in range(9)]

def formatting(a,b,c,d,e):
    ans = '                                                       Generated   ' + b + '   ' + u"\u2713"
    return ans
def show(n,a,path): # iterator, address
    flag = True
    # start = time.time()
    # webAddress = "http://results.bput.ac.in/525_RES/1301106106.html"
    # page=requests.get(webAddress)
    # tree=html.fromstring(page.text)
    # namechk = ''
    # while True:
    #     namechk = tree.xpath("/html/body/table/tr[3]/td/table/tr[2]/td[2]/b/text()")
    #     end = time.time()
    #     if end - start > 3:
    #         break
    # if len(namechk) > 0:
    #     flag = True
    # else:
    #     flag = False

    # del start
    # del end

    if flag:
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
            sgpa = []
            count = []
            if len(name) != 0:
                count = tree.xpath("/html/body/table/tr[5]/td/table/tr[position() > 1]/td[1]/text()")
                del count[-1]
                count = map(int,count)
                if len(count) != 0:
                    sgpa=tree.xpath("/html/body/table/tr[5]/td/table/tr[%s]/td[3]/text()"%str(len(count)+2))

            if name and sgpa:
                if branch[0] == "ELECTRONICS AND INSTRUMENTATION ENGINEERING. ":
                    branch[0] = "INSTRUMENTATION & ELECTRONICS ENGINEERING "

            if name and sgpa:
                grades = tree.xpath("/html/body/table/tr[5]/td/table/tr[position() > 1 and position() < %s]/td[5]/text()"%str(count[-1]+2))
                sub = tree.xpath("/html/body/table/tr[5]/td/table/tr[position() > 1 and position() < %s]/td[3]/text()"%str(count[-1]+2))
                grades = ''.join(grades)

            if name and sgpa:
                res = ind.index(branch[0]+' ')
                if not visited[res]:
                    visited[res] = True
                    for i in sub:
                        subjects[res].append(i)
           
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
    else:
        app2 = Tkinter.Tk()
        app2.withdraw()
        tkMessageBox.showinfo("Error",'Website is down :(')
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
