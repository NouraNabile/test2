from DatabaseLibrary import MainDataBase
from User import User


class Normal_User(User):
    def __init__(self, Nname, Nemail, Npassword):
        super().__init__(Nname, Nemail, Npassword)

    def requestFor_borrowed_book(self, book, numOfborrowed, id):
        count = 0
        count = MainDataBase.get_numOfAvailablesss(book)
        if (count == 0):
            print("sorry this book not available in library")
        elif(count == numOfborrowed):
            print("yes this book is here with the same number of copies")
            print("you can borrow it now MR " + self.name)
            for i in range(0, numOfborrowed):
                MainDataBase.Delete_Book(book)
            MainDataBase.set_list_borrowed_book(book, id)

        elif(count < numOfborrowed):
            print("sorry only copies avalable is " + str(count) +
                  "\nDo you want to take it\n""if yes set y or if it no say n")
            x = input()
            if(x == "y"):
                for i in range(0, count):
                    MainDataBase.Delete_Book(book)
                    MainDataBase.set_list_borrowed_book(book, self.ID)
                print("you can borrow it now MR " + self.name)
            elif(x == "n"):
                print("ok, nice to meet you")
            else:
                print("i cannot under stand .\n try again")

    def requestFor_return_book(self, book, numOfreturn):
        for i in range(0, numOfreturn):
            MainDataBase.set_list_available_book(book)
            MainDataBase.Delete_Book_borrow(book)
        print("Done have a good time ")

    def ExtendLoanBook(self, book, EtendLoan):
        book.extendLoanPeriod(EtendLoan)
