from diction import movies
movies=movies()
def avg(movies):
    av=0
    for i in movies:
        av+=i["imdb"]
    return av/len(movies)
print(avg(movies))