from diction import movies
movies=movies()
def av(movies, n):
    curr=0
    total=0
    for i in movies:
        if i["category"]==n:
            total+=1
            curr+=i['imbd']
    return curr/total
n=str(input())
print(av(movies, n))