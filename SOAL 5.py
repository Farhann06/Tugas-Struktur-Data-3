def countInversionsNaive(arr):
    inv = 0
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    
    return inv

def mergeSort(arr):
    
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr)//2
    
    left, inv_left = mergeSort(arr[:mid])
    right, inv_right = mergeSort(arr[mid:])
    
    merged = []
    i = j = 0
    inv_count = inv_left + inv_right
    
    while i < len(left) and j < len(right):
        
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
    
    merged += left[i:]
    merged += right[j:]
    
    return merged, inv_count


def countInversionsSmart(arr):
    _, inv = mergeSort(arr)
    return inv


data = [8,4,2,1]

print(countInversionsNaive(data))
print(countInversionsSmart(data))