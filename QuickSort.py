cnt = 0
def quicksort(arr)
    global cnt
    if len(arr) <= 1:
        return arr
    p=arr.pop(0)
    menores, mayores = [], []
    for e in arr:
        cnt+=1
        if e<=p:
            menores.append(e)
        else:
            mayores.append(e)
    return quicksort(menores) + [p] + quicksort(mayores)