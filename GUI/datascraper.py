#Anwesh Mohanty

import Tkinter
import sys
from lxml import html
import requests
from Tkinter import *
import math
# import rank_generator
# import rankGenUI

number = 0

def formatting(a,b,c,d,e):
    ans = a + ' '*(30 - len(a)) + b + ' '*15 + c + ' '*(35 - len(c)) + d+'          '+e
    return ans

def show(n,a,path): # iterator, address
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

    grades = tree.xpath("/html/body/table/tr[5]/td/table/tr[position() > 1 and position() < 8]/td[5]/text()")
    grades = ''.join(grades)
    # if name and sgpa:   # by checking for both name and sgpa, we can be sure to filter all empty nodes
    #     print name[0],roll[0],branch[0],sgpa[0]
    #     number += 1
    if name and sgpa:
        print name[0],roll[0],branch[0],sgpa[0],grades
        sys.stdout.close()
        ans = formatting(name[0],roll[0],branch[0],sgpa[0],grades)
        return ans
    else:
        return 0

# rank_generator.calculateRank(number)
# rank_generator.displayRank()
