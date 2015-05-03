import sys
import collections
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')
boy = [[]for i in range(2)]
girl = [[]for i in range(2)]
for i in range(1,198):
    f = False
    s = raw_input()
    if len(s) > 0:
        s = map(str,s.split())
        if s[1][-1] == 'A' or s[1][-1] == 'E' or s[1][-1] == 'I':
            f = True
        r = ''
        for j in range(1,len(s)):
            if '0' <= s[j][0] <= '9':
                if f:
                    girl[0].append(s[j])
                else:
                    boy[0].append(s[j])
                break
            else:
                r += s[j]+" "
        if f:
            girl[1].append(r)
        else:
            boy[1].append(r)
print 'Here are the girls '
for i in range(len(girl[0])):
    print girl[0][i],girl[1][i]
print 'Here are those who are not girls '
for i in range(len(boy[0])):
    print boy[0][i],boy[1][i]
