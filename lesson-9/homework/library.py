class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def __str__(self):
        return f'"{self.title}" by {self.author}'

class Member:
    MAX_BORROW_LIMIT = 3
    
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BORROW_LIMIT:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than {self.MAX_BORROW_LIMIT} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f'"{book.title}" is already borrowed.')
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f'{self.name} borrowed {book}')
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f'{self.name} returned {book}')
        else:
            print(f'{self.name} did not borrow {book}')

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
        print(f'Book added: {book}')
    
    def add_member(self, member):
        self.members.append(member)
        print(f'Member registered: {member.name}')
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f'"{title}" is not available in the library.')