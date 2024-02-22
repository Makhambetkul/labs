def even(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i

n=int(input())
result = [str(num) for num in even(n)]
print(",".join(result))