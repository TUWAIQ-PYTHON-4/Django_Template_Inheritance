
from django.urls import path
import To_Do_listApp.views
urlpatterns = [path('', To_Do_listApp.views.home, name='home'),
               path('about/',To_Do_listApp.views.about, name='about'),

               ]