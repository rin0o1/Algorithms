

import time

#This function is used to find the number before and after the pivot
def GetIndexToPartition(arr, min, max):
    
    MinValueIndex= min-1
    Pivot=arr[max]

    
    for Num in range(min, max):
        #if the current number is smoller than Pivot...
        if arr[Num]<=Pivot:
            #Change the index of the minimum 
            MinValueIndex= MinValueIndex+1
            #switch that number with the number with index "MinValueIndex"
            arr[MinValueIndex], arr[Num]= arr[Num], arr[MinValueIndex]
            
        
    
    Pivot=MinValueIndex+1
    #Move the pivot in the correct position
    arr[max],arr[MinValueIndex+1]= arr[MinValueIndex+1], arr[max] 
    
    return Pivot

def QuickSort(arr, min , max):
    
    
    if min<max:

        #Height= position of the current Pivot
        Pivot= GetIndexToPartition(arr,min, max)
        
        #Order left
        QuickSort(arr,min,Pivot-1)
        #Order right
        QuickSort(arr,Pivot+1,max)
        

t1= time.perf_counter()
arr= [10,7,1,8,9,1,5]
max_= len(arr)-1
min_=0
QuickSort(arr, min_, max_)
print (time.perf_counter()-t1, "time spended")
print(arr[0])
print(arr[-1])
for x in arr:
    print (x)
