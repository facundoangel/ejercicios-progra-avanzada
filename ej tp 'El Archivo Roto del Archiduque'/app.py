def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if(left[i]<=right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        
 
    if(len(right)>j):
        while j < len(right):
            result.append(right[j])
            j+=1

            

    if(len(left)>i):
        while i < len(left):
            result.append(left[i])
            i+=1

            

    return result
 
 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr               # caso base
 
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
 
 
# Prueba:
pergaminos = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(pergaminos))
# Esperado: [3, 9, 10, 27, 38, 43, 82]