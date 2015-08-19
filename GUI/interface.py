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
from PIL import ImageTk,Image

# convert everyting to classes
app = Tk()
app.config(bg = '#%02x%02x%02x' %(78,94,110))
app.title("Generate Student Statistics")

files = ['file1','file2','file3','file4','file5','file6']
# tmp = []
# for i in files:
# 	tmp.append(i+'sub')
# files += tmp
# del tmp
menuVar = StringVar(app)
menuVar.set(files[0])
ProgVar = IntVar(app)
r1 = StringVar(app)
r2 = StringVar(app)
r3 = StringVar(app)
r4 = StringVar(app)



formData = {}
for i in files:
	j = i + '.txt'
	formData[j] = ['130 110 6090','130 110 6110','-1']

"""
start of functions
"""


def InitFiles(menuVar):
	listBox.grid()
	packlogo.grid_remove()
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
		chk.config(bg = 'darkred')
		chk.select()
		chk.toggle()
		# path = menuVar+'.txt'
		# f = os.open(path,os.O_WRONLY|os.O_CREAT) #
		# os.close(f) #
		genRank.config(fg = 'gray',bg='white',state = DISABLED)
		genGrade.config(fg = 'gray',bg='white',state = DISABLED)
		gen.config(state = NORMAL, text = 'Get Student List', fg = 'white',activeforeground = 'white',bg = 'navyblue')
	listBox.grid_remove()
	packlogo.grid()

listFiles = OptionMenu(app,menuVar,*files,command = InitFiles)
listFiles.config(width = 13, font = ('Times New Roman',14,"bold"))
listFiles.grid(row = 16,column = 3)

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

chkVar_rank = IntVar()
chkVar_scrape = IntVar()

def checked():
	ProgVar.set(0)
	if chkVar_rank.get():
		chk.config(bg = 'forestgreen')
		gen.config(text = 'Data Collected !!',fg = 'red',activeforeground = 'red',bg = 'white')
		gen.config(state = DISABLED)
		genRank.config(state = NORMAL,fg = 'white',activeforeground = 'white',bg = 'forestgreen')
		genGrade.config(state = NORMAL,fg = 'white',activeforeground = 'white',bg = 'forestgreen')
	else:
		path = menuVar.get()+'.txt'
		chk.config(bg = 'darkred')
		genRank.config(fg = 'gray',bg='white',state = DISABLED)
		genGrade.config(fg = 'gray',bg ='white',state = DISABLED)
		gen.config(state = NORMAL, text = 'Get Student List', fg = 'white',activeforeground = 'white',bg = 'navyblue')

def student(i,address,path):
	s = rankScraper.show(i,address,path)
	return s

def progress(fact):
	progBar.step(99.99999999999/fact)
	app.update()
	# time.sleep(0.1)

def fileStatus():
	listBox.grid()
	packlogo.grid_remove()
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

def FastGenerate_checker():
	if chkVar_scrape.get():
		chk_scraper.config(bg = 'darkviolet',activebackground = 'darkviolet')
	else:
		chk_scraper.config(bg = 'darkgray',activebackground = 'darkgray')


def getList():
	if not chkVar_scrape.get():
		progBar.config(mode = 'determinate')
		begin = int(''.join(map(str,startRoll.get().split())))
		end = int(''.join(map(str,endRoll.get().split())))
		lbegin = int(''.join(map(str,LstartRoll.get().split())))
		lend = int(''.join(map(str,LendRoll.get().split())))
		fact = float(end-begin)+1
		factL = float(lend-lbegin)+1
		gen.config(text = 'Getting Data', bg = 'darkred')
		address = urlDigit.get()
		path = menuVar.get()+'.txt'
		listBox.grid()
		packlogo.grid_remove()
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

		if end - begin > 10000 or lend - lbegin > 10000:
			tkMessageBox.showinfo("Warning",'Start and End roll formatting different')
			genRank.config(state = DISABLED)
			genGrade.config(state = DISABLED)
			gen.config(state = NORMAL, text = 'Get Student List', fg = 'white',bg = 'navyblue')

		else:
			for i in range(begin,end + 1):
				res = student(i,address,path)
				# time.sleep(0.3)
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
					gen.config(state = NORMAL, text = 'Get Student List', fg = 'white',bg = 'navyblue')
					break
				if res != '0':
					res += '\n'
					listBox.config(state = NORMAL,font = ('Times New Roman',12),width = 80)
					listBox.insert(INSERT,res)
					listBox.see(END)
					listBox.config(state = DISABLED)
				progress(factL)

			if res != '-1':
				gen.config(text = 'Data Collected !!',fg = 'darkgray',bg = 'white')
				gen.config(state = DISABLED)
				genRank.config(state = NORMAL,fg = 'white',bg = 'forestgreen')
				genGrade.config(state = NORMAL,fg = 'white',bg = 'forestgreen')
			else:
				listBox.delete(1.0,END)
			path2 = menuVar.get()+'sub.txt'
			rankScraper.getSubject(path2)

	else:

		packlogo.grid_remove()
		listBox.grid()
		listBox.config(state = NORMAL,font = ('Times New Roman',16,"bold","italic"),width = 40,height = 10)
		listBox.delete(1.0,END)
		listBox.insert(INSERT,' >>>>>>>>>>>>> Fast Generate >>>>>>>>>>>>')
		listBox.see(END)
		listBox.config(state = DISABLED)
		path = menuVar.get()+'.txt'
		begin = int(''.join(map(str,startRoll.get().split())))
		end = int(''.join(map(str,endRoll.get().split())))
		lbegin = int(''.join(map(str,LstartRoll.get().split())))
		lend = int(''.join(map(str,LendRoll.get().split())))
		
		gen.config(text = 'Getting Data', bg = 'darkred')
		address = urlDigit.get()

		open(path,'w').close() #
		res = '0'
		f = os.open(path,os.O_RDWR|os.O_APPEND|os.O_CREAT)
		os.write(f,str(begin) + ' '+ str(end)+' '+ str(lbegin) + ' '+str(lend)+'\n')
		os.close(f)
		formData[path] = [begin,end,address]

		if end - begin > 10000 or lend - lbegin > 10000:
			tkMessageBox.showinfo("Warning",'Start and End roll formatting different')
			genRank.config(state = DISABLED)
			genGrade.config(state = DISABLED)
			gen.config(state = NORMAL, text = 'Get Student List', fg = 'white',bg = 'navyblue')
		else:
			import fastRankScraper
			sys.stdout = open(path,'w')
			print begin,end,lbegin,lend
			res = fastRankScraper.show(begin,end,address,path)
			sys.stdout.close()
			if res == '-1':
					genRank.config(state = DISABLED)
					genGrade.config(state = DISABLED)
					gen.config(state = NORMAL, text = 'Get Student List', bg = 'navyblue',activebackground = 'navyblue')
			if res != '0':
				res += '\n'
				listBox.config(state = NORMAL,font = ('Times New Roman',12),width = 80)
				listBox.insert(INSERT,res)
				listBox.see(END)
				listBox.config(state = DISABLED)
			sys.stdout = open(path,'a')
			res = fastRankScraper.show(lbegin,lend,address,path)
			sys.stdout.close()
			if res != '-1':
				gen.config(text = 'Data Collected !!',fg = 'darkgray',bg = 'white')
				gen.config(state = DISABLED)
				genRank.config(state = NORMAL,bg = 'forestgreen',fg = 'white')
				genGrade.config(state = NORMAL,bg = 'forestgreen',fg = 'white')
			else:
				listBox.delete(1.0,END)
			fastRankScraper.getSubject(menuVar.get()+'sub.txt')

	listBox.grid_remove()
	packlogo.grid()

def getRank():
	from rank_generator import calculateRank,displayRank,getLimit
	begin = int(''.join(map(str,startRoll.get().split())))
	end = int(''.join(map(str,endRoll.get().split())))
	path = menuVar.get()+'.txt'
	if getLimit(path) != 0:
		calculateRank(path)
		displayRank(path)

def getGrade():
	from rankGrade1 import calculateGrade,displayGrade,getSubjectData,getLimit
	begin = int(''.join(map(str,startRoll.get().split())))
	end = int(''.join(map(str,endRoll.get().split())))

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
		packlogo.grid()
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


def exportData():
	source = menuVar.get() + '.txt'
	destination = exportPath.get()
	import exportToExcel
	exportToExcel.export(source,destination)

def LimRoll(x):
    f = False
    s = x.get()
    if len(s) > 12:
        s = s[:-1]
        x.delete(0,END)
        x.insert(0,s)
    if len(s) == 3:
        x.insert(INSERT,' ')
    if len(s) == 7:
        x.insert(INSERT,' ')
    x.icursor(INSERT)

Grid.rowconfigure(app,0,weight = 1)
Grid.columnconfigure(app,0,weight = 1)

r1.trace("w",lambda name,index,mode,r1 = r1: LimRoll(startRoll))
r2.trace("w",lambda name,index,mode,r2 = r2: LimRoll(endRoll))
r3.trace("w",lambda name,index,mode,r3 = r3: LimRoll(LstartRoll))
r4.trace("w",lambda name,index,mode,r4 = r4: LimRoll(LendRoll))

"""
Start of buttons
"""

Label(app, text = 'Digit of URL', font = ('Times New Roman',14,"bold"),fg = 'white', bg = '#%02x%02x%02x' %(128,0,0)\
      ,relief = RAISED).grid(row = 2, column = 2)
Label(app, text = '      Start Roll     ', font = ('Times New Roman',14,'bold'), fg = 'white',bg = '#%02x%02x%02x' %(128,0,0)\
      ,relief = RAISED).grid(row = 4, column = 1)
Label(app, text = '     End Roll     ', font = ('Times New Roman', 14,'bold'), fg = 'white',bg = '#%02x%02x%02x' %(128,0,0)\
      ,relief = RAISED).grid(row = 4, column = 3)
Label(app, text = '    LE Start Roll   ', font = ('Times New Roman', 14,'bold'), fg = 'white',bg = '#%02x%02x%02x' %(128,0,0)\
      ,relief = RAISED).grid(row = 6, column = 1)
Label(app, text = '    LE End Roll   ', font = ('Times New Roman', 14,'bold'), fg = 'white',bg = '#%02x%02x%02x' %(128,0,0)\
      ,relief = RAISED).grid(row = 6, column = 3)
Label(app, text = 'Anwesh Mohanty', font = ('Times New Roman', 14,'bold'), fg = 'white',bg = '#%02x%02x%02x' %(128,0,0)\
      ,relief = RAISED).grid(row = 7, column = 2)
Label(app, text = 'Export Data to Excel File', font = ('Times New Roman',12,"bold"),fg = 'white', bg = '#%02x%02x%02x' %(128,0,0)\
      ,relief = RAISED).grid(row = 18, column = 1)


sampleAddress = Text(app, height = 1)
sampleAddress.insert(INSERT,'         Eg : http://results.bput.ac.in/525_RES/1301106106.html')
sampleAddress.grid(row = 3 ,column = 2)
sampleAddress.tag_add('url','1.40','1.43')
sampleAddress.tag_config('url',foreground = 'blue')
sampleAddress.config(state = DISABLED)


urlDigit = Entry(app, justify = CENTER, bg = '#f5f5f5', relief = SUNKEN)
startRoll = Entry(app, justify = CENTER, bg = '#f5f5f5', relief = SUNKEN,textvariable = r1)
endRoll = Entry(app, justify = CENTER, bg = '#f5f5f5', relief = SUNKEN,textvariable = r2)
LstartRoll = Entry(app, justify = CENTER, bg = '#f5f5f5', relief = SUNKEN,textvariable = r3)
LendRoll = Entry(app, justify = CENTER, bg = '#f5f5f5', relief = SUNKEN,textvariable = r4)
exportPath = Entry(app, justify = CENTER, bg = '#f5f5f5', relief = SUNKEN,width = 100)

endRoll.insert(0,"130 110 6110")
startRoll.insert(0,"130 110 6090")
LendRoll.insert(0,"142 110 6021")
LstartRoll.insert(0,"142 110 6011")
urlDigit.insert(0,"525")
exportPath.insert(0,"Example.csv")

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
exportPath.grid(row = 18,column = 2)

listBox = ScrolledText(app, height = 15, width = 114,font = ('Times New Roman',9))
listBox.grid(row = 10,column = 2)
listBox.config(state = DISABLED)


gen = Button(app,command = getList, text = 'Get  Student  List', font = ('Times New Roman',16,'bold'), bg = 'navyblue', \
    fg = 'white', activeforeground = 'white',activebackground = '#D1FFBD', relief = RAISED)
gen.grid(row = 15, column = 2)

genRank = Button(app,command = getRank, text = 'Generate   Ranks', font = ('Times New Roman',16,'bold'), bg = 'white', \
    fg = 'gray', activeforeground = 'gray', relief = RAISED, state = DISABLED)
genRank.grid(row = 16, column = 2)

genGrade = Button(app,command = getGrade, text = 'Generate  Grades', font = ('Times New Roman',16,'bold'), bg = 'white', \
    fg = 'gray', activeforeground = 'gray', relief = RAISED, state = DISABLED)
genGrade.grid(row = 17, column = 2)

editFile = Button(app,command = ModFile, text = 'Modify File', font = ('Times New Roman',14), bg = 'white', \
    fg = 'gray', activeforeground = 'gray', relief = RAISED,width = 16)
editFile.grid(row = 15, column = 1)
editFile.config(state = DISABLED)

chkFile = Button(app,command = fileStatus, text = 'Status of Current File', font = ('Times New Roman',14), bg = 'white', \
    fg = 'blue', activeforeground = 'blue', relief = RAISED)
chkFile.grid(row = 16, column = 1)

progBar = ttk.Progressbar(orient = HORIZONTAL, length = 500,variable = ProgVar,mode = "determinate",maximum = 100)
progBar.grid(row = 6, column = 2)

chk = Checkbutton(app, text = 'Already Generated',variable = chkVar_rank, font = ('Times New Roman', 14,"bold"),bg = 'darkred',\
 fg = 'white', relief = RAISED, command = checked)
chk.grid(row = 15, column = 3)

chk_scraper = Checkbutton(app, text = 'Fast Generate',variable = chkVar_scrape, font = ('Times New Roman', 14,"bold"),bg = 'darkgray',\
 activebackground = 'darkgray',fg = 'white',activeforeground = 'white', relief = RAISED,width = 13, command = FastGenerate_checker)
chk_scraper.grid(row = 17, column = 3)

clrFile = Button(app,command = clrFile, text = 'Erase File Data', font = ('Times New Roman',14,"bold"), bg = 'white', \
    fg = 'red', activeforeground = 'red', relief = RAISED, width = 15)
clrFile.grid(row = 17, column = 1)

exportButton = Button(app,command = exportData, text = 'Export', font = ('Times New Roman',10,"bold"), bg = 'forestgreen', \
    fg = 'white', activeforeground = 'white', relief = RAISED, width = 24,height = 1)
exportButton.grid(row = 18, column = 3)

logo = ImageTk.PhotoImage(Image.open("Biju-patnaik-university.logo.jpg"))
listBox.grid_remove()
packlogo = Label(app,image = logo)
packlogo.grid(row = 10, column = 2)
# app.geometry('1375x500')
app.resizable(width = False, height = False)
app.mainloop()
