import requests


BOOK_BASE_URI='http://localhost:8081/api/v1/books/'

'''
class Book:
    def __init__(self,id,name,price,cat,publisher):
        self.id=id
        self.name=name
        self.price=price
        self.cat=cat
        self.publisher=publisher

'''

class BookOps:

    @staticmethod
    def get_all_books():
        return requests.get(BOOK_BASE_URI).json()

    @staticmethod
    def get_single_book(bid):
        return requests.get(BOOK_BASE_URI+str(bid)).json()

    @staticmethod
    def insertbook(bk=None):
        bk_json = {
              "name": bk.name,
              "price": bk.price,
              "cat": bk.cat,
              "active": "Y",
              "publisher": 99991
            }
        response = requests.post(BOOK_BASE_URI,json=bk_json)
        if response.status_code>=200 and response.status_code<=300:
            return "Success"
        return "Failed..!"


    @staticmethod
    def updatebook(bk=None):
        bk_json = {
              "name": 'AAAAAA',
              "price": 12283.34,
              "cat": 'Good',
              "active": "Y",
              "publisher": 99991
            }
        response = requests.put(BOOK_BASE_URI+str(7776)+"/",json=bk_json)
        if response.status_code>=200 and response.status_code<=300:
            return "Success"

        print(response.status_code)
        return "Failed..!"

    @staticmethod
    def delete_book(bid=0):
        response = requests.delete(BOOK_BASE_URI+str(17776))
        if response.status_code>=200 and response.status_code<=300:
            return "Success"

        print(response.status_code)
        return "Failed..!"

if __name__ == '__main__':
    print(BookOps.get_all_books())
