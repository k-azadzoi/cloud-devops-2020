#   More practice with Python classes

class Movie:

    def __init__(self, title, genre, year):
        self.title = title
        self.genre = genre
        self.year = year

    def full_desc(self):
        return "The movie you requested is {}, {}. It was made in {}".format(self.title, self.genre, self.year)


#   instance method that will print out the full description of a movie

first_movie = Movie("Jurassic Park", "Sci-Fi", "1994")
print(first_movie.full_desc())
# The output will be "The movie you requested is Jurassic Park, Sci-Fi. It was made in 1994"
