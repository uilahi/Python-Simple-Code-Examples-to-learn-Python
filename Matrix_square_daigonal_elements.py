def square(l):
    v=[]
    d = 0
    e = -1
    k=[]
    for i in l:
        k.append(i[d]**2)
        d += 1

    for i in (l):
        k.append(i[e]**2)
        e -= 1
    return k




s = square([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(s)