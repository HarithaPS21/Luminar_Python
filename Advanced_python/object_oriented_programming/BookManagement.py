
class Books:
    books={
    "alchemist":{"Book_name":"alchemist","author":"paulo","price":200,"av_copies":100,"sold":10},
    "halfgirlfriend":{"Book_name":"hfg","author":"chethan","price":300,"av_copies":300,"sold":200},
    "rainraising":{"Book_name":"rainraising","author":"nirupama","price":350,"av_copies":10,"sold":340}

    }
    def findBook(self,Book_name):
        self.Book_name=Book_name
        for book in self.books:
             print(self.books[book]["Book_name"],self.books[book]["av_copies"])

    def sortAuthor(self):
        res = sorted(books.items(), key=lambda x: x[0]["sold"], reverse=True)
        for val in res:
            print(val[1]["author"])

obj=Books()
obj.findBook("alchemist")

obj.sortAuthor()



