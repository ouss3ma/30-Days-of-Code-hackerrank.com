import sys
import re


N = int(input().strip())
l=[]
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.search(r"@gmail.com$",emailID) is not None:l.append(firstName)
l.sort()
for i in range (len(l)):
    print(l[i])
