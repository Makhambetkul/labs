from diction import movies
movies=movies()
def sublist(movies):
    s=[]
    for i in movies:
        if i["imbd"]>=5.5:
            s.append(i)
        return s
print(sublist(movies))