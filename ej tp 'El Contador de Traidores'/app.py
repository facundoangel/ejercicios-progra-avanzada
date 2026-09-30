def merge_contar(left, right):
    # Combina left y right ordenadamente.
    # Cuenta las inversiones que "cruzan" la división.
    result = []
    inversiones = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            # left[i] > right[j] → inversión
            # ??? ¿cuántas inversiones agrega este paso?
            inversiones+=len(left)-i
            result.append(right[j]); j += 1
    result += left[i:] + right[j:]
    return result, inversiones
 
def contar_inversiones(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left,  inv_l = contar_inversiones(arr[:mid])
    right, inv_r = contar_inversiones(arr[mid:])
    merged, inv_m = merge_contar(left, right)
    return merged, inv_l + inv_r + inv_m


print(contar_inversiones([2, 4, 1, 3, 5]))