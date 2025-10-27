
import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
print (data)
x =int(input("write a year and I will tell all movies created after that year"))
# for i in range(x+1 ,2026):
#     print(len(data("titles")))
for movies in data:
    print(movies["title"])