def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i

n=int(input())
result = [str(num) for num in even(n)]
print(",".join(result))