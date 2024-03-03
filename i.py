class Private:
    def add_book(self, book):
        raise NotImplementedError
    
    def remove_book(self, book):
        raise NotImplementedError

    def overdue_books(self, num):
        raise NotImplementedError

    def reports(self):
        raise NotImplementedError
      

class Public:
    def search_title(self, title):
        raise NotImplementedError

    def search_author(self, author):
        raise NotImplementedError

    def search_genre(self, genre):
        raise NotImplementedError

    def return_book(self, book):
        raise NotImplementedError

    def borrow_book(self, book):
        raise NotImplementedError  
    

class Users(Public):
    def search_title(self, title):
        print("Title Found")

    def search_author(self, author):
        print("Author Found")

    def search_genre(self, genre):
        print("Genre Found")

    def return_book(self, book):
        print( book +" Book Returned")

    def borrow_book(self, book):
        print(book +" Book Borrowed") 


class Librarian( Public,Private):
    def search_title(self, title):
        print("Title Found")

    def search_author(self, author):
        print("Author Found")

    def search_genre(self, genre):
        print("Genre Found")

    def return_book(self, book):
        print( book +" Book Returned")

    def borrow_book(self, book):
        print(book +" Book Borrowed") 

    def add_book(self, book):
        print( book +" Book added")

    def remove_book(self, book):
        print(book +" Book removed")

    def overdue_books(self, num):
        print(str(num) +" Overdue Books")

    def reports(self):
        print("Reports")

def user_Access(public):
    pass
def librarian_Access(private):
    pass


Kaylee = Librarian()
Matt = Users()

Kaylee.add_book("Lord of the Rings")
Matt.search_title("Lord of the Rings")