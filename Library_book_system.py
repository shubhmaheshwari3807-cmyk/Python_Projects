class Book():
    def __init__(self, title, author, available=True):
        self.title=title
        self.author=author
        self.available=available

    def borrow(self):
        self.available=False
        print("The book is not avaiable")

    def ret(self):
        self.available=True
        print("The book is avaiable")

book1=Book("How I Met Your Mother", "Mr. X", available=True)
book1.borrow()
book1.ret()
