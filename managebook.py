class Book:
    year = int
    author = str
    title = str

    def __init__(self,a,t,y):
        self.year = y
        self.author = a
        self.title = t

        
    def display(self):
        print("------------Book Details-------------")
        print("Title: %s\nAuthor: %s\nYear: %d\n"%(self.title, self.author, self.year) )


Bobj1 = Book("J.R.R. Tolkien", "The Hobbit", 1937)
Bobj1 = Book("J.K Rowling", "Harry Potter", 1997)


print("First Book Details")
Bobj1.display()


print("Second Book Details")
Bobj1.display()