import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
print (data)
x =(input("write a year and I will tell all movies created in that year"))
print(x(data))
