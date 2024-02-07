def unique(L):
    d=[]
    for i in L:
        if i not in d:
            d.append(i)
    print(*d)
unique(input().split())