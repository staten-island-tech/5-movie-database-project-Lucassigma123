
import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)
# for movies in data:
#     print(movies["title"]) 
# x =int(input("write a year and I will tell all movies created after that year"))
# for movies in data:
#  if (movies["year"]) > x:  
#      print(movies["title"],(movies["year"]))

# y=int(input("give me a year i will print all movies after that year"))
# for movies in data:
#    if(movies["year"])>y:
#       print (movies["title"],(movies["year"]))

# s=int(input("give me another year i will print all movies before that year"))  
# for movies in data:
#    if(movies["year"])<s:
#       print (movies["title"],(movies["year"]))

# f=int(input("give me another year i will print all movies in that year"))  
# for movies in data:
#    if(movies["year"])== f:
#       print (movies["title"],(movies["year"]))

# k=input("give me a specific movie and i will print all results")
# for movies in data:
   
#    if k.lower() in movies["title"].lower():
#       print(movies["title"]),print(movies["year"])

p=input("give me a genre")
for movies in data:
    if p in (movies["genres"]):
        print(movies["title"]),(movies["year"])