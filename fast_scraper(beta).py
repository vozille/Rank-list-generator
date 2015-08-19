import sys
from lxml import html
import grequests
import requests
import math
import tkMessageBox
import os
import time

# import rank_generator
# import rankGenUI


number = 0
ind = ["MECHANICAL ENGINEERING ","ELECTRICAL ENGINEERING ","CIVIL ENGINEERING ","INSTRUMENTATION & ELECTRONICS ENGINEERING "\
,"COMPUTER SCIENCE & ENGINEERING ","BIO TECHNOLOGY ","INFORMATION TECHNOLOGY ","TEXTILE ENGINEERING ","FASHION TECHNOLOGY ","BACHELOR OF ARCHITECTURE "]
visited = [False]*len(ind)

subjects = [[]for i in range(len(ind))]

def show(start,stop,a,path): # iterator, address
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
            
            pages = [grequests.get("http://results.bput.ac.in/525_RES/"+"%s.html"%str(i)) for i in range(start,stop+1)]
            pages = grequests.map(pages,size = 80)
            trees = [html.fromstring((pages[i]).text) for i in range(len(pages))]
            names = [trees[i].xpath("/html/body/table/tr[3]/td/table/tr[2]/td[2]/b/text()") for i in range(len(pages))]
            branches = [trees[i].xpath("/html/body/table/tr[3]/td/table/tr[4]/td[2]/b/text()") for i in range(len(pages))]
            rolls = [trees[i].xpath("/html/body/table/tr[3]/td/table/tr[1]/td[2]/text()") for i in range(len(pages))]
            grades = [''.join(trees[i].xpath("/html/body/table/tr[5]/td/table/tr[position() > 1]/td[5]/text()")) for i in range(len(pages))]
            sgpa = [trees[i].xpath("/html/body/table/tr[5]/td/table/tr[%s]/td[3]/text()"%str(len(grades[i])+2)) for i in range(len(pages))]
            sub = [trees[i].xpath("/html/body/table/tr[5]/td/table/tr[position() > 1]/td[3]/text()") for i in range(len(pages))]

            for i in range(len(pages)):
                if names[i] and sgpa[i]:
                    print names[i][0],rolls[i][0],branches[i][0],grades[i],sgpa[i][0]
                    res = ind.index(branches[i][0]+' ')
                    if not visited[res]:
                        visited[res] = True
                        for j in sub[i]:
                            subjects[res].append(j)
                        del subjects[res][-1]
            useless = requests.get("http://results.bput.ac.in/525_RES/1301106106.html")

            return '0'
        except requests.ConnectionError:
            app2 = Tkinter.Tk()
            app2.withdraw()
            tkMessageBox.showinfo("Error",'Slow/No Internet Connection. Try normal generate')
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
# show(1301106000,1301106100,525,'foo.txt')
# getSubject('foo2.txt')
