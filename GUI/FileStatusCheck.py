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

def getStats(path):
    data = []
    cnt = 0
    foo = os.open(path,os.O_RDWR|os.O_CREAT)
    sys.stdin = open(path,'r')
    start,stop = 0,0
    while True:
        try:
            r = raw_input()
            if cnt == 0:
                data.append(r)
                r = map(str,r.split())
                try:
                    start = r[0]
                    end = r[1]
                except IndexError:
                    start = '0'
                    end = '0'
            else:
                data.append(r)
            cnt += 1
        except EOFError:
            sys.stdin.close()
            os.close(foo)
            if cnt == 0:
                app2 = Tkinter.Tk()
                app2.withdraw()
                tkMessageBox.showinfo("Error",'File is empty. Generate List before proceeding')
                return cnt,data
            else:
                app2 = Tkinter.Tk()
                app2.withdraw()
                res = "File Contains data of students with roll from "+start + ' to ' + end
                tkMessageBox.showinfo("Status",res)
                return cnt,data
