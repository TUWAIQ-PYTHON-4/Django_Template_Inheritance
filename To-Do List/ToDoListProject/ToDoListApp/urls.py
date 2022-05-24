from django.urls import path
import ToDoListApp.views

#from ToDoListProject.ToDoListApp import views

urlpatterns = [
    path('about/', ToDoListApp.views.about),
    path('home/', ToDoListApp.views.home),
    ]
#urlpatterns = [
 #   path('', views.home, name='home'),
  #  path('about/', views.about, name='about'),
#]
