def calculate_factorial(integer):
    i=0
    a=1
    while i!=integer:
        i+=1
        a=a*i
    print(a)
b=int(input())
calculate_factorial(b)