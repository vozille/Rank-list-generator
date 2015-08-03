import Tkinter
from Tkinter import *
import sys
from functools import partial
import rankScraper
import ttk
import time
from ScrolledText import ScrolledText
import os
import tkMessageBox

# convert everyting to classes
app = Tk()
app.config(bg = '#708090')
app.title("Rank Generator")

files = ['file1','file2','file3','file4','file5','file6']
# tmp = []
# for i in files:
# 	tmp.append(i+'sub')
# files += tmp
# del tmp
menuVar = StringVar(app)
menuVar.set(files[0])
ProgVar = IntVar(app)

formData = {}
for i in files:
	j = i + '.txt'
	formData[j] = ['1301106100','1301106110','-1']

"""
start of functions
"""


def InitFiles(menuVar):
	listBox.grid()
	editFile.config(fg = 'gray',activeforeground = 'gray',state = DISABLED)
	listBox.config(state = NORMAL)
	listBox.delete(1.0,END)
	listBox.config(state = DISABLED)

	i = menuVar + '.txt'
	startRoll.delete(0,END)
	startRoll.insert(END,formData[i][0])
	endRoll.delete(0,END)
	endRoll.insert(END,formData[i][1])
	urlDigit.delete(0,END)
	urlDigit.insert(END,formData[i][2])

	if formData[i][2] == '-1':
		listBox.delete(1.0,END)
		chk.config(fg = 'red',activeforeground = 'red')
		chk.select()
		chk.toggle()
		# path = menuVar+'.txt'
		# f = os.open(path,os.O_WRONLY|os.O_CREAT) #
		# os.close(f) #
		genRank.config(state = DISABLED)
		genGrade.config(state = DISABLED)
		gen.config(state = NORMAL, text = 'Get Student List', fg = 'blue',activeforeground = 'blue')
	listBox.grid_remove()

listFiles = OptionMenu(app,menuVar,*files,command = InitFiles)
listFiles.grid(row = 16,column = 3)

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

chkVar = IntVar()
def checked():
	ProgVar.set(0)
	if chkVar.get():
		chk.config(fg = 'green',activeforeground = 'green')
		gen.config(text = 'Data Collected !!',fg = 'darkgreen',activeforeground = 'green')
		gen.config(state = DISABLED)
		genRank.config(state = NORMAL,fg = 'green',activeforeground = 'green')
		genGrade.config(state = NORMAL,fg = 'green',activeforeground = 'green')
	else:
		path = menuVar.get()+'.txt'
		
		chk.config(fg = 'red',activeforeground = 'red')
		genRank.config(state = DISABLED)
		genGrade.config(state = DISABLED)
		gen.config(state = NORMAL, text = 'Get Student List', fg = 'blue',activeforeground = 'blue')

def student(i,address,path):
	s = rankScraper.show(i,address,path)
	return s

def progress(fact):
	progBar.step(99.99999999999/fact)
	app.update()
	# time.sleep(0.1)

def fileStatus():
	listBox.grid()
	path = menuVar.get() + '.txt'
	editFile.config(fg = 'red',activeforeground = 'red',state = NORMAL)
	import RankFileCheck
	x,res = RankFileCheck.getStats(path)
	if x != 0:
		listBox.config(state = NORMAL,font = ('Times New Roman',9),width = 114)
		listBox.delete(1.0,END)
		for i in range(x-1):
			if i != x-2:
				listBox.insert(INSERT,res[i]+'\n')
			else:
				listBox.insert(INSERT,res[i])
		listBox.config(state = DISABLED)

def getList():
	
	begin = int(startRoll.get())
	end = int(endRoll.get())
	lbegin = int(LstartRoll.get())
	lend = int(LendRoll.get())
	fact = float(end-begin)+1
	factL = float(lend-lbegin)+1
	gen.config(text = 'Getting Data',fg = 'red', activeforeground = 'red')
	address = urlDigit.get()
	path = menuVar.get()+'.txt'
	listBox.grid()
	listBox.config(state = NORMAL)
	listBox.delete(1.0,END)
	listBox.insert(INSERT,'                          ****************Start of non-LE students**************** \n\n')
	listBox.config(state = DISABLED)
	# f = os.open(path,os.O_RDWR|os.O_APPEND|os.O_CREAT) #
	# os.ftruncate(f,0) #
	# os.lseek(f,0,os.SEEK_SET) #
	# os.close(f)

	open(path,'w').close() #
	res = '0'
	f = os.open(path,os.O_RDWR|os.O_APPEND|os.O_CREAT)
	os.write(f,str(begin) + ' '+ str(end)+' '+ str(lbegin) + ' '+str(lend)+'\n')
	os.close(f)
	formData[path] = [begin,end,address]

	for i in range(begin,end + 1):
		res = student(i,address,path)
		if res == '-1':
			genRank.config(state = DISABLED)
			genGrade.config(state = DISABLED)
			gen.config(state = NORMAL, text = 'Get Student List', fg = 'blue',activeforeground = 'blue')
			break
		if res != '0':
			res += '\n'
			listBox.config(state = NORMAL,font = ('Times New Roman',12),width = 80)
			listBox.insert(INSERT,res)
			listBox.see(END)
			listBox.config(state = DISABLED)
		progress(fact)

	listBox.config(state = NORMAL,font = ('Times New Roman',12),width = 80)
	listBox.insert(INSERT,'                          *****************Start of LE students****************** \n\n')
	listBox.see(END)
	listBox.config(state = DISABLED)

	for i in range(lbegin,lend + 1):
		res = student(i,address,path)
		if res == '-1':
			genRank.config(state = DISABLED)
			genGrade.config(state = DISABLED)
			gen.config(state = NORMAL, text = 'Get Student List', fg = 'blue',activeforeground = 'blue')
			break
		if res != '0':
			res += '\n'
			listBox.config(state = NORMAL,font = ('Times New Roman',12),width = 80)
			listBox.insert(INSERT,res)
			listBox.see(END)
			listBox.config(state = DISABLED)
		progress(factL)

	if res != '-1':
		gen.config(text = 'Data Collected !!',fg = 'darkgreen',activeforeground = 'green')
		gen.config(state = DISABLED)
		genRank.config(state = NORMAL,fg = 'green',activeforeground = 'green')
		genGrade.config(state = NORMAL,fg = 'green',activeforeground = 'green')
	else:
		listBox.delete(1.0,END)
	path2 = menuVar.get()+'sub.txt'
	rankScraper.getSubject(path2)

	listBox.grid_remove()

def getRank():
	from rank_generator import calculateRank,displayRank,getLimit
	begin = int(startRoll.get())
	end = int(endRoll.get())
	path = menuVar.get()+'.txt'
	if getLimit(path) != 0:
		calculateRank(path)
		displayRank(path)

def getGrade():
	from rankGrade1 import calculateGrade,displayGrade,getSubjectData,getLimit
	begin = int(startRoll.get())
	end = int(endRoll.get())

	path = menuVar.get()+'.txt'
	path2 = menuVar.get()+'sub.txt'
	if getLimit(path) != 0:
		getSubjectData(path2)
		calculateGrade(path)
		displayGrade(path)


def ModFile():
	if editFile.config('text')[-1] == 'Save File':
		listBox.config(state = NORMAL)
		useless = listBox.get(1.0,END)
		editFile.config(text = 'Saved !!', fg = 'blue',activeforeground = 'blue')
		app.update()
		time.sleep(0.5)
		editFile.config(text = 'Modify File',fg = 'red',activeforeground = 'red')
		
		path = menuVar.get()+'.txt'
		f = os.open(path,os.O_RDWR|os.O_APPEND|os.O_CREAT)
		sys.stdout = open(path,'w')
		print useless
		sys.stdout.close()
		os.close(f)
		listBox.delete(1.0,END)
		listBox.grid_remove()
	else:
		editFile.config(text = 'Save File',fg = 'green',activeforeground = 'green')
		listBox.config(state = NORMAL)

	# exit(0)

def clrFile():
	if tkMessageBox.askyesno("Erase File","Are you sure ?"):
		listBox.config(state = NORMAL)
		listBox.delete(1.0,END)
		listBox.config(state = DISABLED)
		chk.config(fg = 'red',activeforeground = 'red')
		chk.select()
		chk.toggle()
		path = menuVar.get()+'.txt'
		sys.stdout = open(path,'w')
		f = os.open(path,os.O_RDWR|os.O_APPEND|os.O_CREAT)
		sys.stdout.close()
		os.close(f)

Grid.rowconfigure(app,0,weight = 1)
Grid.columnconfigure(app,0,weight = 1)

"""
Start of buttons
"""

Label(app, text = 'Digit of URL', font = ('Times New Roman',14,"bold"),fg = 'white', bg = 'maroon',relief = RAISED).grid(row = 2, column = 2)
Label(app, text = '      Start Roll     ', font = ('Times New Roman',14,'bold'), fg = 'white',bg = 'maroon',relief = RAISED).grid(row = 4, column = 1)
Label(app, text = '     End Roll     ', font = ('Times New Roman', 14,'bold'), fg = 'white',bg = 'maroon',relief = RAISED).grid(row = 4, column = 3)
Label(app, text = '    LE Start Roll   ', font = ('Times New Roman', 14,'bold'), fg = 'white',bg = 'maroon',relief = RAISED).grid(row = 6, column = 1)
Label(app, text = '    LE End Roll   ', font = ('Times New Roman', 14,'bold'), fg = 'white',bg = 'maroon',relief = RAISED).grid(row = 6, column = 3)
Label(app, text = 'Anwesh Mohanty', font = ('Times New Roman', 14,'bold'), fg = 'white',bg = 'maroon',relief = RAISED).grid(row = 7, column = 2)

sampleAddress = Text(app, height = 1)
sampleAddress.insert(INSERT,'         Eg : http://results.bput.ac.in/525_RES/1301106106.html')
sampleAddress.grid(row = 3 ,column = 2)
sampleAddress.tag_add('url','1.40','1.43')
sampleAddress.tag_config('url',foreground = 'blue')
sampleAddress.config(state = DISABLED)


urlDigit = Entry(app, justify = CENTER, bg = '#f5f5f5', relief = SUNKEN)
startRoll = Entry(app, justify = CENTER, bg = '#f5f5f5', relief = SUNKEN )
endRoll = Entry(app, justify = CENTER, bg = '#f5f5f5', relief = SUNKEN)
LstartRoll = Entry(app, justify = CENTER, bg = '#f5f5f5', relief = SUNKEN)
LendRoll = Entry(app, justify = CENTER, bg = '#f5f5f5', relief = SUNKEN)

endRoll.insert(END,"1301106110")
startRoll.insert(END,"1301106090")
LendRoll.insert(END,"1421106021")
LstartRoll.insert(END,"1421106011")
urlDigit.insert(END,"525")

endRoll.config(font = 'bold')
startRoll.config(font = 'bold')
LendRoll.config(font = 'bold')
LstartRoll.config(font = 'bold')
urlDigit.config(font = 'bold')

startRoll.grid(row = 5, column = 1)
endRoll.grid(row = 5, column = 3)
LstartRoll.grid(row = 7, column = 1)
LendRoll.grid(row = 7, column = 3)
urlDigit.grid(row = 4, column = 2)


listBox = ScrolledText(app, height = 15, width = 114,font = ('Times New Roman',9))
listBox.grid(row = 10,column = 2)
listBox.config(state = DISABLED)


gen = Button(app,command = getList, text = 'Get Student List', font = ('Times New Roman',18), bg = 'white', \
    fg = 'blue', activeforeground = 'blue',activebackground = '#D1FFBD', relief = RAISED)
gen.grid(row = 15, column = 2)

genRank = Button(app,command = getRank, text = 'Generate Ranks', font = ('Times New Roman',18), bg = 'white', \
    fg = 'gray', activeforeground = 'gray', relief = RAISED, state = DISABLED)
genRank.grid(row = 16, column = 2)

genGrade = Button(app,command = getGrade, text = 'Generate Grades', font = ('Times New Roman',18), bg = 'white', \
    fg = 'gray', activeforeground = 'gray', relief = RAISED, state = DISABLED)
genGrade.grid(row = 17, column = 2)

editFile = Button(app,command = ModFile, text = 'Modify File', font = ('Times New Roman',14), bg = 'white', \
    fg = 'gray', activeforeground = 'gray', relief = RAISED)
editFile.grid(row = 15, column = 1)
editFile.config(state = DISABLED)

chkFile = Button(app,command = fileStatus, text = 'Status of Current File', font = ('Times New Roman',14), bg = 'white', \
    fg = 'blue', activeforeground = 'blue', relief = RAISED)
chkFile.grid(row = 16, column = 1)

progBar = ttk.Progressbar(orient = HORIZONTAL, length = 500,variable = ProgVar,mode = "determinate",maximum = 100)
progBar.grid(row = 6, column = 2)

chk = Checkbutton(app, text = 'Already Generated',variable = chkVar, font = ('Times New Roman', 14),fg = 'red',\
 activeforeground = 'red', command = checked)
chk.grid(row = 15, column = 3)

clrFile = Button(app,command = clrFile, text = 'Erase File Data', font = ('Times New Roman',14), bg = 'white', \
    fg = 'red', activeforeground = 'red', relief = RAISED)
clrFile.grid(row = 17, column = 1)

listBox.grid_remove()

# app.geometry('1375x500')
app.resizable(width = False, height = False)
app.mainloop()

