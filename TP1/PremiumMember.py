from Member import Member

class PremiumMember(Member):
    def __init__(self, name):
        super().__init__(name)  
        self.borrow_limit = 5  
        
        
    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.borrow_limit:
            return False
        return super().borrow_book(book)  