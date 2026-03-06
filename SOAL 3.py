def insertionSort(arr):
    comp = swap = 0
    
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            comp += 1
            swap += 1
        
        arr[j+1] = key
    
    return comp + swap


def selectionSort(arr):
    comp = swap = 0
    n = len(arr)
    
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1,n):
            comp += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swap += 1
    
    return comp + swap


def hybridSort(arr, threshold=10):
    
    if len(arr) < threshold:
        ops = insertionSort(arr)
        method = "Insertion Sort"
    else:
        ops = selectionSort(arr)
        method = "Selection Sort"
    
    return arr, ops, method


data = [9,5,1,4,3,8,6]

print(hybridSort(data))