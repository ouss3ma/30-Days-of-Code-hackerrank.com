i=int(input())

for i in range (i):
    s=input()
    a1=""
    a2=""
    for i in range (len(s)):
        if i%2==0:
            a1=a1+s[i]
        else:
            a2=a2+s[i]
    a=a1+" "+a2
    print(a)
