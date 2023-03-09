from datetime import date
from datetime import timedelta


class Book():
    __id_book = 0

    def __init__(self, title, Author, id_user):
        super().__init__()
        self.title = title
        self.author = Author
        self.id_user = id_user
        self.numOfAvailable = 0
        self.loanPeriod = 7
        self.count = 0
        Book.__id_book += 1
        self.bookID = Book.__id_book

    def getAuthor(self):
        return self.author

    def setAuthor(self, value):
        self.author = value

    def getTitle(self):
        return self.title

    def setTitle(self, value):
        self.title = value

    def getLoanPeriod(self):
        return self.loanPeriod

    def extendLoanPeriod(self, value):
        self.loanPeriod = value
        today = date.today()
        print("OK,sure you can borrow " + self.title)
        print("Today's date:", today)
        Enddate = today + timedelta(days=value)
        print("Ending date :", Enddate)
