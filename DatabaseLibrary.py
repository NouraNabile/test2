class MainDataBase:  # react as data base
    list_available_book = []
    list_borrowed_book = []
    list_user = []
    count = 0

    @classmethod
    def set_list_available_book(cls, book):
        cls.list_available_book.append(book)

    @classmethod
    def set_list_borrowed_book(cls, book, id):
        book.id_user = id
        cls.list_borrowed_book.append(book)

    @classmethod
    def get_list_available_book(cls):
        print(f"{len(cls.list_available_book)} Avalible book : ")
        for book in cls.list_available_book:
            print(book.getTitle() + " for " + book.getAuthor())

    @classmethod
    def get_numOfAvailable(cls, book):
        for i in range(0, len(cls.list_available_book)):
            itrbook = cls.list_available_book[i]
            if book.title == itrbook.title:
                cls.count += 1
        print(f'numOfAvailable : {book.title} = {cls.count}')

    @classmethod
    def get_numOfAvailablesss(cls, book):
        c = 0
        for i in range(0, len(cls.list_available_book)):
            itrbook = cls.list_available_book[i]
            if book.getTitle() == itrbook.getTitle():
                c += 1
        return c

    @classmethod
    def get_list_borrowed_book(cls):  # by UserID getName of user??
        print(f"{len(cls.list_borrowed_book)} borrowed book : ")
        for book in cls.list_borrowed_book:
            print(book.getTitle() + " by user " + str(book.id_user))

    @classmethod
    def set_user(cls, user):
        cls.list_user.append(user)

    @classmethod
    def get_user(cls, id_user):
        return cls.list_user.get(id_user+1)

    @classmethod
    def Delete_Book(cls, book):
        for i in range(0, len(cls.list_available_book)):
            itrbook = cls.list_available_book[i]
            if book.getTitle() == itrbook.getTitle():
                cls.list_available_book.remove(book)
            break

    @classmethod
    def get_list_user(cls):
        print('users:')
        for i in range(0, len(cls.list_user)):
            print(cls.list_user[i].name)

    @classmethod
    def Delete_Book_borrow(cls, book):
        cls.list_borrowed_book.remove(book)
