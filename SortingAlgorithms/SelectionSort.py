def selectionsort(alist):
    for i in range(len(alist) - 1):
        smallest_index = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest_index]:
                smallest_index = j
        alist[i], alist[smallest_index] = alist[smallest_index], alist[i]
    return alist

alist = [20, 50, 10, 30, 60, 40]
selectionsort(alist)
print(selectionsort(alist))
