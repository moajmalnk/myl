from django.urls import path

from mylibrary.views import *

app_name = 'mylibrary'

urlpatterns = [
    path('', home, name='home'),
    path('book/<int:id>/', detail_view, name='detail'),
    path('add_book/', add_book, name='add_book'),
    path('update/<int:id>/', update_book, name='update'),
    path('delete/<int:id>/', delete_book, name='delete'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('add_patron/', add_patrons, name='add_patron'),
    path('all_patrons/', all_patrons, name='all_patrons'),
    path('update_patron/<int:id>/', update_patron, name='update_patron'),
    path('delete_patron/<int:id>/', delete_patron, name='delete_patron'),
    path('newspaper/', news_paper, name='newspaper'),
    path('program/<int:id>/', programmes, name='program'),
    path('category/', all_book_category, name='all_book_category'),
    path('category/<slug:c_slug>/', all_book_category, name='books_by_category'),

]
