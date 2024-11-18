class Book:
    def __init__(self, title, author):

        self.title = title
        self.author = author
        self.is_available = True 
        
    def __str__(self):
        if self.is_available == True:
            available="available"
        else:
            available="not available" 
        return f"{self.title} by {self.author} - ({available})"
    
    
    def borrow(self):
        
        if self.is_available == True:
            self.is_available = False
            return True
        else:
            return False  
    
    def return_book(self):
      
        self.is_available = True   
        
