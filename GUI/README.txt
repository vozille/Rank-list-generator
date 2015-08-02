First things first.. find the application..
It's named rankgenui in the dist folder, double click to open it..

Great..
Now lets move on to the functionalities of each and every button. 

_____________________________________________________________________________________________________________________________________________
***URL digit : open the link of say 2nd semester result of this academic year. Now look closely on the url on top of the browser, there will be a 3 digit number. Enter that number. 
-------------

***Start Roll(normal) : Enter the starting roll of the batch. For CET, it is xx01106000 where xx = last two digit of the batch year : Eg for 2013 batch, its 1301106000. You can enter any roll as the starting roll, but that would lead to incomplete results.

	It can also be used for B.Arch, there roll format is xx02106000 (for CET )
--------------

***End Roll(normal): Enter the ending roll of the batch. Dont worry, you dont need to know the exact value. Just enter a large enough roll so that you are 100% sure no one gets missed.
	
	Typically, for CET, for 2013 and newer batches, xx01106700 is sufficient. For older batches, you can safely keep limit as xx01106400
---------------

***Start Roll(LE : Lateral Entry) : Trust me, I really wanted to combine this..(even my ex gf had problems with such segregation, but that's another story). But, unfortunately, iterating through 10^9 numbers to reach Lateral Entry students esp with requests, will take much too long(hours may be)., so had to split it up.

	Lateral Entry roll formats are yy21106000 (for CET), where yy = xx + 1.
---------------

***End Roll(LE : Lateral Entry) : The end roll of lateral entry students. Incase you dont want to or dont need to find out their grades, just choose a value strictly less than the start roll. ( you can apply the same principle in the normal roll, say you just want to evaluate performance of LE students)

----------------

***File(drop down file chooser) : You can store results in one of six files. To select a file, just click the file1(default) in lower right corner and select file to store the data. 

	>>> Please DO NOT select files named 'FileSub.txt' , they are meant for storing subjects.
----------------

***Get Student List : Gets data of students whose roll lies in range of the values provided in the roll boxes. Changes to 'Data Collected' when extraction is complete or when 'Already generate' is clicked

----------------

***Generate Rank : Generates Rank List and shows result in a new window.
----------------

***Generate Grade : Generates Grade Distribution List and shows result in a new window.
----------------

*** Already Generated : Check to skip collecting data and proceed to showing rank/grade for student data stored in the selected file. Disables collecting student data and enables 'Generate rank/Grade'. If file is empty, clicking on 'Generate rank/grade' will display an error message.
-----------------

***Status Of Current File : Displays the contents of current file in textbox. Enables Modify File button.
----------------

***Modify File : Modify contents of displayed File. Not recommended.
	>>> one case it may be used is when you generate list of normal and LE separately, and then you decide to combine it.
	
Clicking on it changes button to save file. Do the modifications(if any) and click the 'Save' button.
----------------

***Erase File: Erases content of selected File. 
	>>> Note : Clicking 'Get Student List' automatically erases any previous data in file.
----------------
_______________________________________________________________________________________________________________________________________________

When you open the application, the default lay-out is presented in such a way that clicking 'Get student List' generates a sample student list.

------------
Exceptions :
	1. If app takes too long to show any activity after clicking 'get student list' , force close the application
When this happens, the site is unresponsive. Try later(1-2 days later)

	//TODO add more here
------------


Any doubts/bugs, you may mail me : anwesh063@gmail.com
