def binary_search(alist, key):
    start = 0
    end = len(alist) - 1

    while start < end:
        mid = (start + end)//2
        print(start,end,mid)
        if key < alist[mid]:
            print(1)
            end = mid

        elif key > alist[mid]:
            print(2)
            start = mid + 1
        else:
            print(3)
            return mid
    return -1

alist = [10, 20, 30, 40, 50, 60, 70, 80, 90]
key = 5
returned_value = binary_search(alist,key)
if returned_value == -1:
    print("Not Found")
else:
    print(f"Element Found at {returned_value}")