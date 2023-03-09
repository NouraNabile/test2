from User import User
from DatabaseLibrary import MainDataBase


class Lib_User(User):
    def __init__(self, Lname, Lemail, password):
        super().__init__(Lname, Lemail, password)

    def Add_Book(self, value):
        MainDataBase.set_list_available_book(value)

    def set_list_borrowed_book(self, value):
        MainDataBase.list_borrowed_book(value)

        # librarian have apility only to see data for all user&librarian
    def get_list_user(self):
        return MainDataBase.get_user()

    def set_list_user(self, value):
        MainDataBase.set_user(value)

    def get_user(self, id):
        return MainDataBase.get_user(id)

    def get_list_user(self,):
        return MainDataBase.get_list_user()

    def Delete_Book(self, book):
        MainDataBase.Delete_Book(book)
