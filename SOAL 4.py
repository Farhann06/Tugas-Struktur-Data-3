def mergeThreeSortedLists(A, B, C):
    
    i = j = k = 0
    result = []
    
    while i < len(A) or j < len(B) or k < len(C):
        
        values = []
        
        if i < len(A):
            values.append((A[i], 'A'))
        if j < len(B):
            values.append((B[j], 'B'))
        if k < len(C):
            values.append((C[k], 'C'))
        
        val, source = min(values)
        
        result.append(val)
        
        if source == 'A':
            i += 1
        elif source == 'B':
            j += 1
        else:
            k += 1
    
    return result


print(mergeThreeSortedLists([1,5,9],[2,6,10],[3,4,7]))