class Book:
  def __init__(self, title, author, publication_year):

    self.title = title
    self.author = author
    self.publication_year = publication_year
    self.borrowed = False 

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
