from django.urls import path
import ToDoListApp.views
urlpatterns = [
    path('',ToDoListApp.views.base),
    path('home/',ToDoListApp.views.home),
    path('about/',ToDoListApp.views.about) ,

]