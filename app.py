
import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
# for movies in data:
#     print(movies["title"]) 
x =int(input("write a year and I will tell all movies created after that year"))
for movies in data:
    if movies ["year"] > x:  
        print(movies["title"],(movies["year"]))