import sys
import os
def export(source,destination):
	f = open(destination,'w')
	f.truncate()
	f.close()
	import csv
	with open(destination,'wb') as csvFile:
		fields = ['Name','Roll','Branch','SGPA','Grades']
		writer = csv.DictWriter(csvFile,fieldnames = fields)
		writer.writeheader()

		sys.stdin = open(source,'r')
		useless = raw_input()
		del useless
		while True:
			try:
				foo = map(str,raw_input().split())
				ff = True
				name = ''
				branch = ''
				grade = ''
				roll = 'abcd'
				sgpa = 'df'
				for j in range(len(foo)):
					if 48 <= ord(foo[j][0]) <= 57:
						if ff:
							roll = foo[j]
							ff = False
						else:
							sgpa = foo[j]
					else:
						if ff:
							name += str(foo[j]) + ' '
						else:
							if j != len(foo)-1:
								branch += str(foo[j]) + ' '
							else:
								grade += str(foo[j])
				writer.writerow({fields[0]: name, fields[1]: roll, fields[2]: branch, fields[3]: sgpa, fields[4]: grade})
			except EOFError:
				sys.stdin.close()
				break
				
