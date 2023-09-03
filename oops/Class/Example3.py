class Movie:
    def __init__(self,movie,hero,heroine):
        self.movie=movie
        self.hero=hero
        self.heroine=heroine
    def info(self):
        print("The movie name is {}".format(self.movie))
        print("Hero is :",self.hero)
        print("Heroine is :",self.heroine)
list_of_movies=[]
while True:
    movie=input("Enter movie name : ")
    hero=input("Enter Hero name : ")
    heroine=input("Enter Heroine name : ")
    list_of_movies.append(Movie(movie,hero,heroine))
    Limit=input("Enter No or Yes: ")
    if Limit.lower()=='no':
        break
for movie in list_of_movies:
    movie.info()