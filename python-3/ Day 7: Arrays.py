n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

s=""
i=n-1
while i>=0:
    s=s+str(arr[i])+" "
    i=i-1
print(s)
