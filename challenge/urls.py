from django.urls import path
from challenge import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index2'),
    path('details/<id>/<id2>', views.details, name='details'),
    path('bookmark/<id>', views.bookmark, name='bookmark'),
    path('bookmarked', views.bookmarked, name='bookmarked'),
    path('remove/<id>', views.remove, name='remove'),
]
