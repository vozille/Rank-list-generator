import Tkinter
from Tkinter import *
import sys
from PIL import Image, ImageTk
from functools import partial
import rankApp
import ttk
import time
from ScrolledText import ScrolledText
import os

# convert everyting to classes

app = Tk()
app.config(bg = '#708090')
app.title("Rank Generator")
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

endRoll.insert(END,"1301106109")
startRoll.insert(END,"1301106104")
LendRoll.insert(END,"1402106200")
LstartRoll.insert(END,"1402106000")
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


listBox = ScrolledText(app, height = 10, width = 120)
listBox.grid(row = 10,column = 2)
listBox.config(state = DISABLED)

files = ['file1','file2','file3','file4','file5','file6']
menuVar = StringVar(app)
menuVar.set(files[0])
ProgVar = IntVar(app)

formData = {}
for i in files:
	j = i + '.txt'
	formData[j] = ['1301106100','1301106110','-1']


def foo(menuVar):
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
		# path = menuVar.get()+'.txt'
		# f = os.open(path,os.O_WRONLY|os.O_CREAT)
		# os.close(f)
		genRank.config(state = DISABLED)
		genGrade.config(state = DISABLED)
		gen.config(state = NORMAL, text = 'Get Student List', fg = 'blue',activeforeground = 'blue')


listFiles = OptionMenu(app,menuVar,*files,command = foo)
listFiles.grid(row = 17,column = 3)


# logo = Text(app, width = 30, height = 15)
# logo.grid(row = 6, column = 2)
# pic = Image.open('Biju-patnaik-university.logo.jpg')
# pic_src = ImageTk.PhotoImage(pic)
# logo.image_create(END, image = pic_src)

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
	s = rankApp.show(i,address,path)
	return s

def progress(fact):
	progBar.step(99.99999999999/fact)
	app.update()
	# time.sleep(0.1)

def getList():
	listBox.config(state = NORMAL)
	listBox.insert(INSERT,'NAME                          ROLL                     BRANCH                              SGPA          GRADES\n\n')
	begin = int(startRoll.get())
	end = int(endRoll.get())
	fact = float(end-begin)+1
	gen.config(text = 'Getting Data',fg = 'red', activeforeground = 'red')
	address = urlDigit.get()
	path = menuVar.get()+'.txt'

	f = os.open(path,os.O_RDWR|os.O_APPEND|os.O_CREAT)
	os.ftruncate(f,0)
	os.lseek(f,0,os.SEEK_SET)
	os.close(f)

	f = os.open(path,os.O_RDWR|os.O_APPEND|os.O_CREAT)
	os.write(f,str(begin) + ' '+ str(end)+'\n')
	os.close(f)
	formData[path] = [begin,end,address]
	for i in range(begin,end + 1):
		res = student(i,address,path)
		if res != 0:
			res += '\n'
			listBox.insert(INSERT,res)
		progress(fact)
	gen.config(text = 'Data Collected !!',fg = 'darkgreen',activeforeground = 'green')
	gen.config(state = DISABLED)
	genRank.config(state = NORMAL,fg = 'green',activeforeground = 'green')
	genGrade.config(state = NORMAL,fg = 'green',activeforeground = 'green')

def getRank():
	from rank_generator import calculateRank,displayRank
	begin = int(startRoll.get())
	end = int(endRoll.get())
	path = menuVar.get()+'.txt'
	calculateRank(path)
	displayRank()

def getGrade():
	from rankGrade1 import calculateGrade,displayGrade
	begin = int(startRoll.get())
	end = int(endRoll.get())
	path = menuVar.get()+'.txt'
	calculateGrade(path)
	displayGrade()

def clearData():
	listBox.delete(1.0,END)
	chk.config(fg = 'red',activeforeground = 'red')
	chk.select()
	chk.toggle()
	path = menuVar.get()+'.txt'

	f = os.open(path,os.O_RDWR|os.O_APPEND|os.O_CREAT)
	os.ftruncate(f,0)
	os.lseek(f,0,os.SEEK_SET)
	os.close(f)
	# exit(0)

	genRank.config(state = DISABLED)
	genGrade.config(state = DISABLED)
	gen.config(state = NORMAL, text = 'Get Student List', fg = 'blue',activeforeground = 'blue')

gen = Button(app,command = getList, text = 'Get Student List', font = ('Times New Roman',18), bg = 'white', \
	fg = 'blue', activeforeground = 'blue',activebackground = '#D1FFBD', relief = RAISED)
gen.grid(row = 15, column = 2)

genRank = Button(app,command = getRank, text = 'Generate Ranks', font = ('Times New Roman',18), bg = 'white', \
	fg = 'gray', activeforeground = 'gray', relief = RAISED, state = DISABLED)
genRank.grid(row = 17, column = 2)

genGrade = Button(app,command = getGrade, text = 'Generate Grades', font = ('Times New Roman',18), bg = 'white', \
	fg = 'gray', activeforeground = 'gray', relief = RAISED, state = DISABLED)
genGrade.grid(row = 19, column = 2)

clrFile = Button(app,command = clearData, text = 'Clear Data', font = ('Times New Roman',14), bg = 'white', \
	fg = 'red', activeforeground = 'red', relief = RAISED)
clrFile.grid(row = 17, column = 1)

progBar = ttk.Progressbar(orient = HORIZONTAL, length = 500,variable = ProgVar,mode = "determinate",maximum = 100)
progBar.grid(row = 6, column = 2)

chk = Checkbutton(app, text = 'Already Generated',variable = chkVar, font = ('Times New Roman', 14),fg = 'red',\
 activeforeground = 'red', command = checked)
chk.grid(row = 15, column = 3)

app.geometry('1275x500')
app.resizable(width = False, height = False)
app.mainloop()

