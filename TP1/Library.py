from Book import Book
from RegularMember import RegularMember
from PremiumMember import PremiumMember

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
            new_book = Book(title, author)
            self.books.append(new_book)
            print(f" Added book: {new_book}")

    def add_member(self, member_type, name):
            if member_type == "regular":
                new_member = RegularMember(name)
            elif member_type == "premium":
                new_member = PremiumMember(name)
            else:
                print("Incorrect")
                return

            self.members.append(new_member)
            print(f" Added member: {new_member.name}")

    def list_books(self):
            print("Library books:")
            if len(self.books) == 0:
                print("Vide")
            else:
                for book in self.books:
                    print(book)    
                    
    def find_book(self, title):

            for book in self.books:
                if book.title == title:
                    return book
            return None 
                
    def find_member(self, name):
            for member in self.members:
                if member.name.lower() == name.lower():
                    return member
            return None                              