class Book:
    def __init__(self,title, author,year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    def description(self):
        return f"'{self.title}' by {self.author}, published in {self.year_published}"
    def is_classic(self):
        if self.year_published < 1970:
            return True
        return False 
    
    
book_1 = Book("Mansifer","Lily Alberts",2007)
print(Book.description(book_1))
print(Book.is_classic(book_1))

