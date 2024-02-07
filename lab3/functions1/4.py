def filter_prime(a):
    f=list(filter(lambda x: sum([x%i==0 for i in range(1, x+1)])==2, a))
    print(f)
filter_prime([13, 17, 18, 24, 91, 127])