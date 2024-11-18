from Book import Book
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = [] 


    def borrow_book(self, book):
        if book.borrow():         
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed {book.title}")
            return True
        else:
            print(f"Le livre '{book.title}' n'est pas disponible")
            return False


    def return_book(self, book): 
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            print(f"{self.name} has returned {book.title}")
        else:
            print(f"{book.title} n'est pas emprunté")    


    def list_borrowed_books(self):
            
            if len(self.borrowed_books)==0:
                print(f"{self.name}has not borrowed any books.")
            else:    
                print(f"{self.name} has borrowed the following books:") 
                for book in self.borrowed_books:
                    print(f"{book.title} ") 
                          