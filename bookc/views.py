
from django.shortcuts import render
from bookc.models import Book,get_dummyBook

def welcome_book_page(req):
    return render(req,'book.html',
                  {
                    "bk": get_dummyBook(),
                    "greet" : "Welcome to BookInfo",
                      "booklist": Book.abooks.all(),
                  })

def save_book(req):
    if req.method=='POST':
        userfilledinfo = req.POST#all info -- id==0  id>0
        bid = int(req.POST['bid']) #114
        book = Book(bname=userfilledinfo['bnm'],
                    bprice=userfilledinfo['bprice'],
                    bqty=userfilledinfo['bqty'],
                    bauthor=userfilledinfo['bauthor'],
                    bremarks=userfilledinfo['bremarks'])
        msg ='Added Successfully..!'
        if bid>0:
            book.id=bid
            msg = "Updated Successfully...!"

        book.save()
    return render(req,'book.html',
                  {
                      "bk":get_dummyBook(),
                      "actionmsg":msg,
                      "booklist":Book.abooks.all(),
                  })

def fetch_for_edit(req,bid):
    return render(req,'book.html',
                  {
                      "bk":Book.abooks.get(id=bid),
                      "booklist":Book.abooks.all(),
                  })


def delete_Book(req,bid):
    bk = Book.books.get(id=bid)
    if bk:
        bk.delete()
    return render(req,'book.html',
                  {
                      "bk": get_dummyBook(),
                     "actionmsg":"BookInfo deleted..!",
                      "booklist":Book.abooks.all(),
                  })

#-----------------------PRODUCER------------------------
from bookc.rest_api_consume import *

class BookInfo:
    def __init__(self,id=0,name='',price=0.0,cat=''):
        self.id=id
        self.name=name
        self.price=price
        self.cat=cat


def convert_to_books(resjsons):
    booklist = []
    for json in resjsons:
        booklist.append(BookInfo(json['id'],json['name'],json['price'],json['cat']))
    return booklist

def welcome_pr_page(req):
    return render(req,'book_pr.html',
                  {
                    'booklist' :  convert_to_books(BookOps.get_all_books()),
                    'bk':BookInfo()
                  })


def save_pr_book(req):
    if req.method=='POST':
        userfilledinfo = req.POST#all info -- id==0  id>0
        bid = int(req.POST['id']) #114
        book = BookInfo(name=userfilledinfo['name'],
                    price=userfilledinfo['price'],
                    cat=userfilledinfo['cat'])

        if bid>0:
            book.id=bid
            BookOps.updatebook(book)
            msg = "Updated Successfully...!"
        else:
            BookOps.insertbook(book)
            msg = "Saved..!"
    return render(req,'book_pr.html',
                  {
                      "bk":BookInfo(),
                      "actionmsg":msg,
                      "booklist":convert_to_books(BookOps.get_all_books()),
                  })