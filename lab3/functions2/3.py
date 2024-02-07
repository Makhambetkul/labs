from diction import movies
movies=movies()
def cat(movies, ct):
    d=[]
    for i in movies:
        if i["category"]==ct:
            d.append(i)
    return d;
print(cat(movies, input()))