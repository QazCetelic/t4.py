p=0
g=['_']*9
while 1:
 print(3*'\t\t%s %s %s\n'%(*g,))
 g[int(input())-1]='OX'[p]
 p^=1