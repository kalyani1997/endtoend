from django.urls import path
from bookc.views import *
urlpatterns = [
    path('welcome/', welcome_book_page),
    path('save/', save_book),
    path('edit/<int:bid>', fetch_for_edit),
    path('delete/<int:bid>', delete_Book),
    path('prbk/welcome/',welcome_pr_page),
    path('prbk/save/',save_pr_book)
]