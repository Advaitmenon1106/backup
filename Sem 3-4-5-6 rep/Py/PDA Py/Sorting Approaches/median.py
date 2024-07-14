def partition(ar, l, h):
    pivot = ar[h]
    i = l
    for j in range (l, h):
        if ar[j]<pivot:
            i+=1
            ar[i], ar[j] = ar[j], ar[i]
    ar[h], ar[i] = ar[i], ar[h]
    return i+1