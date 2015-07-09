
import sys
from lxml import html
import requests
import math


#sys.stdout = open('output.txt','w')
for i in range(1201106000,1201106350): # iterator, address
    page=requests.get("http://results.bput.ac.in/524_RES/%s.html"%str(i))

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

    # grades = tree.xpath("/html/body/table/tr[5]/td/table/tr[position() > 1 and position() < 8]/td[5]/text()")
    # print ''.join(grades)
    if name and sgpa:   # by checking for both name and sgpa, we can be sure to filter all empty nodes

        # print name[0],' ',roll[0],' ',branch[0],' ',sgpa[0] #check progress
        # print ''
        print name[0],roll[0],branch[0],sgpa[0]
