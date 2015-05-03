import sys
import collections
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
s = { 'O' : 0, 
      'E' : 0,
      'A' : 0, 
      'B' : 0, 
      'C' : 0, 
      'D' : 0, 
      'F' : 0, 
      'S' : 0,
}

for i in range(99):
    k = map(str,raw_input().split())
    if len(k) == 0:
        continue
    else:
        if int(k[0]) not in girls:
            s[k[3]] += 1
foo = ['O','E','A','B','C','D','F','S']
for i in foo:
    print " Grade : "+i+" ",str(s[i])+'/96'
print len(girls)
