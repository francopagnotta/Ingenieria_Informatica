# 4. Sol tiene una lista de diccionarios donde guarda todas las películas que vió. La información que tiene
# para cada una es: el nombre de la serie, año en que salió, y la puntuación que le puso del 1 al 10. Hace
# mucho que quiere que Tomás empiece a ver las películas que ella considera que son las mejores que
# vio.
# Hacer una función que reciba el diccionario de las películas que vió Sol, y que devuelva una nueva lista
# de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.

movies = [
  {"name": "The Shawshank Redemption", "release": 1994, "score": 10},
  {"name": "The Godfather", "release": 1972, "score": 9.5},
  {"name": "The Dark Knight", "release": 2008, "score": 9},
  {"name": "The Lord of the Rings: The Return of the King", "release": 2003, "score": 9},
  {"name": "Schindler's List", "release": 1993, "score": 9.4},
  {"name": "Pulp Fiction", "release": 1994, "score": 8.9},
  {"name": "12 Angry Men", "release": 1957, "score": 8.9},
  {"name": "Fight Club", "release": 1999, "score": 8.8},
  {"name": "Whiplash", "release": 2014, "score": 8.5},
  {"name": "Inception", "release": 2010, "score": 8.8},
]

def getMovieListByScore(movie_list, score):
    return list(
        filter(lambda movie : movie["score"] > score, movie_list)
	)

score = 7
filtered_movies = getMovieListByScore(movies, score)

print(f"list of movies with a score above {score}:")

for movie in filtered_movies:
    print(movie)
