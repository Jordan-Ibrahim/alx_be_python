class Book:
    def _init_(self, author, title):
        self.author = author
        self.title = title
        self._is_checked_out = False

    def is_checked_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

  #  def is_available(self):
        return not self._is_checked_out

 #   def _str_(self):
 #       return f"'{self.title}' by {self.author}"


class Library:
    def _init_(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {book}")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {book}")
                return
        print(f"Book '{title}' is not checked out.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")