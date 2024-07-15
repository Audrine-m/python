class Book:

  def __init__(self, title, author, publication_year):

    self.title = title
    self.author = author
    self.publication_year = publication_year
    self.borrowed = False  # Initially, the book is not borrowed

  def borrow_book(self):

    self.borrowed = True
    print(f"{self.title} has been borrowed.")

  def return_book(self):

    self.borrowed = False
    print(f"{self.title} has been returned.")

  def display_info(self):

    borrowed_status = "Borrowed" if self.borrowed else "Available"
    print(f"\nTitle: {self.title}")
    print(f"Author: {self.author}")
    print(f"Publication Year: {self.publication_year}")
    print(f"Borrowed Status: {borrowed_status}")


class LibraryMember(Book):
  def __init__(self, member_id, name):

    self.member_id = member_id
    self.name = name
    self.borrowed_books = []  # List to store borrowed books

  def borrow_book(self, book):

    if not book.borrowed:
      self.borrowed_books.append(book)
      book.borrow_book()  # Update book status in Book class
      print(f"{book.title} has been borrowed by {self.name}.")
    else:
      print(f"{book.title} is not available for borrowing.")

  def return_book(self, book):

    if book in self.borrowed_books:
      self.borrowed_books.remove(book)
      book.return_book()  # Update book status in Book class
      print(f"{book.title} has been returned by {self.name}.")
    else:
      print(f"{self.name} has not borrowed {book.title}.")

  def display_info(self):

    print(f"\nMember ID: {self.member_id}")
    print(f"Name: {self.name}")
    if self.borrowed_books:
      print("Borrowed Books:")
      for book in self.borrowed_books:
        print(f"- {book.title}")
    else:
      print("No books currently borrowed.")


# Example
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979)
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)

member1 = LibraryMember(12345, "Audrine Mohamed")

member1.borrow_book(book1)
member1.borrow_book(book2) 

