def get_max(a, b, c):
    max=0
    if a>=b and a>=c:
        max=a
    elif b>=a and b>=c:
        max=b
    elif c>=a and c>=b:
        max=c
    print(max)
a=1
b=10
c=10
get_max(a, b, c)