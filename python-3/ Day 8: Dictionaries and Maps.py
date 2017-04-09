PB={}
n=int(input())
for i in range (n):
    a=[str(n) for n in input().strip().split(" ") ]
   
    PB[a[0]]=int(a[1])
    
#for line in sys.stdin.readlines():
for i in range (n):
    line=input()

    if line in PB :
        print(line+"="+str(PB[line]))
    else:
        print("Not found")
