def prime(list):
    d=[]
    for i in list:
        if i%2!=0 or i%3!=0 or i%5!=0 or i%7!=0 or i%9!=0:
            d.append(i)
    print(d)


list=[23, 43, 24, 25]
prime(list)