a=int(input())
b=int(input())
def s(a,b):
    for i in range(a, b):
        yield i**2

result = [str(num) for num in s(a, b)]
print(",".join(result))