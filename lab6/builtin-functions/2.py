word=input()
a=0
b=0
for i in word:
    if ord(i)>=97 and ord(i)<=122:
        a+=1
    elif ord(i)>=65 and ord(i)<=90:
        b+=1
print(a, b)