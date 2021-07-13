class Book:
    library_name='ABC Library'                # Static variable........defined inside a class......related to class
    def setval(self,book_name,author,pages):  # Instance variable.......defined inside a method....related to method
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printval(self):
        print(self.book_name)                 # Instance variable.......accessed using self keyword
        print(self.author)
        print(self.pages)
        print(Book.library_name)              # Static variable..........accessed using class name

book1=Book()
book1.setval("Python","Sreeraj",400)
book1.printval()

book2=Book()
book2.setval("Java","Anandu",412)