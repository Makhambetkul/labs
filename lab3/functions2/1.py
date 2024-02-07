from diction import movies
movies = movies()
for i in movies:
    if i["imdb"] >= 5.5:
        print(True)
    else:
        print(False)