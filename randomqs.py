import random
import time 

def partition(arr,l,h):
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h], arr[i+1]
    return i+1

def randomized_partition(arr,l,h):
    pivot = arr[random.randint(l,h)]
    i = l-1
    arr[h],pivot = pivot,arr[h]
    for j in range(l,h):
        if arr[j] <= pivot:
            i += 1 
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1

def quickSort(arr,l,h):
    if l<h:
        pi = partition(arr,l,h)
        quickSort(arr,l,pi-1)
        quickSort(arr,pi+1,h)

def randomizedQuickSort(arr,l,h):
    if l<h:
        pi = randomized_partition(arr,l,h)
        quickSort(arr,l,pi-1)
        quickSort(arr,pi+1,h)
        
arr = [random.randint(1,1000) for i in range(15)]
print(arr)
for i in range(3):
    print("iteration: ",i+1)
    start = time.time()
    randomizedQuickSort(arr,0,len(arr)-1)
    print("randomized qs: ",arr)
    end = time.time()
    print("time: ",end-start)






