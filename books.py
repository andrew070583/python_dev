class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author =author
    def __eq__(self, other):
        return self.name and self.year and self.author == other.name and other.year and other.author

    def add_review(self, review):
        self.review = review

    def show_reviews(self):
        print( '{}'.format( self.review))

book1 = Book('Kapitoshka', 1970, 'lelin')
book2 = Book('Kapitoshka', 1971, 'lelin')
book1.add_review('Cool')
book2.add_review('Fuuu')
print(Book.__eq__(book1,book2))
book2.show_reviews()

