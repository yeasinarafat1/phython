class Library:
    def __init__(self) :
        self.noBokks = 0
        self.books = []
    def addBooks(self,book):
        self.books.append(book)
        self.noBokks = len(self.books)
    def showInfo(self):
        print(f"The library has {self.noBokks} Books")
l1 = Library()
while True:
    mode = int(input("1 for see the book list & 2 for add books"))
    if(mode==1):
        l1
