
from django.db import models

# Create your models here.

class ActiveBooks(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active='Y')


class Book(models.Model):
    bname = models.CharField('book_name',max_length=100)
    bprice = models.FloatField('book_price')
    bqty = models.IntegerField('book_qty')
    bauthor = models.CharField('book_author', max_length=100)
    bremarks = models.CharField('book_remarks', max_length=100)
    active = models.CharField('is_active', max_length=10    ,default='Y')
    books = models.Manager()
    abooks = ActiveBooks()


def get_dummyBook():
    return Book(id=0, bname='', bqty=0, bauthor='', bprice=0.0, bremarks='')