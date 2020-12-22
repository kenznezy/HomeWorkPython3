"""Создать класс Book: id, Название, Автор (ы), Издательство, Год издания, Количество страниц, Цена, Тип переплета.
Функции-члены реализуют запись и считывание полей (проверка корректности).
Создать список объектов. Вывести:
a)	список книг заданного автора;
b)	список книг, выпущенных после заданного года."""


class Book:
    def __init__(self, id, name, author, publisher, year, pages, price, type):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__publisher = publisher
        self.__year = year
        self.__pages = pages
        self.__price = price
        self.__type = type

    def getid(self):
        return self.__id

    def getname(self):
        return self.__name

    def getauthor(self):
        return self.__author

    def getpublisher(self):
        return self.__publisher

    def getyear(self):
        return self.__year

    def getpages(self):
        return self.__pages

    def getprice(self):
        return self.__price

    def gettype(self):
        return self.__type

    def showbookinfo(self):
        print("\nid:\t", self.getid(), "\nname\t",
              self.getname(), "\nauthor:\t", self.__author, "\npublisher:\t", self.__publisher, "\nyear:\t",
              self.__year, "\npages:\t", self.__pages, "\nprice:\t", self.__price, "\ntype:\t", self.__type, "\n \n \n")


class Bookshelf:
    __list_books = []

    def addbook(self, newbook):
        self.__list_books.append(newbook)

    def searchbyauthor(self, author):
        print("By author:")
        results = list(filter(lambda x: x.getauthor() == author, self.__list_books))
        if len(results) == 0:
            print("No records found.")
            return
        for i in results:
            i.showbookinfo()

    def searchbyyear(self, year):
        print("After "+str(year)+" year :")
#        results = list(filter(lambda x: x.getyear().find(year) != -1, self.__list_books))
        results = list(filter(lambda x: x.getyear() > year, self.__list_books))
        if len(results) == 0:
            print("No records found.")
            return
        for i in results:
            i.showbookinfo()


Book = [
    Book("3788", "Robinson Crusoe", "Danielle Dafoe", "Penguin", "1775", "400", "9.99", "Hard"),
    Book("1277", "Catcher in the Rye", "Gerome Sallinger", "O'reilly", "1952", "250", "12.99", "Soft"),
    Book("1337", "1984", "George Orwell", "Oxford", "1946", "300", "5.99", "Pocket"),
    Book("9628", "Bible", "God", "Self-published", "33", "666", "59.99", "Hard")
          ]


listall = Bookshelf()

for i in range(len(Book)):
    listall.addbook(Book[i])

listall.searchbyauthor("God")

listall.searchbyyear("1800")
