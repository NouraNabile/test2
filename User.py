from DatabaseLibrary import MainDataBase


class User:
    __id_user = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        User.__id_user += 1
        self.ID = User.__id_user
        self.password = password

    def searchFor_book(self, book):
        num = MainDataBase.get_numOfAvailablesss(book)
        if num >= 1:
            print("your book is avalible , there are " + str(num) + " copies")
        else:
            print("sorry, its not here yet")


# p1 = User("mohamed", "mohamed@gmail.com", "2554")
# p2 = User("ahmed", "ahmed@gmail.com", "7894")
# p3 = User("amer", "amer@gmail.com", "9512")

# print(p1.ID)
# print(p2.ID)
# print(p3.ID)
