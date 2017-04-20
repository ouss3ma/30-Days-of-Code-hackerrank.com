n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
numberOfSwaps = 0;

for i in range(n) :
    
    
    
    for j in range (n-1) :
        # Swap adjacent elements if they are in decreasing order
        if a[j] > a[j + 1] :
            a[j], a[j + 1]=a[j+1], a[j ]
            numberOfSwaps+=1;
            
    # If no elements were swapped during a traversal, array is sorted
    if numberOfSwaps == 0 :
        break;
    



print ("Array is sorted in",numberOfSwaps,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[n-1])
