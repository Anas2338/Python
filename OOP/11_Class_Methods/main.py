class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
book1 = Book("The Wizard Of Oz")
book2 = Book("The SMC Bible")

print(Book.get_total_books())