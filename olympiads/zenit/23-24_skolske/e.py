n = int(input())
films = []
for i in range(n):
    films.append(int(input()))
films.sort()
if len(films) <= 2:
    print(0)
else:
    uselessfilm=films.pop()
    film = films.pop()
    number_of_trailers=film-1
    if number_of_trailers > len(films):
        result = len(films)
    else:
        result = number_of_trailers
    print(result)