
from django.urls import path
from . import views
urlpatterns = [

   path('',views.home),
   path('login',views.login),
   path('reg',views.registration),
   path('update',views.update),
   path('search',views.search),
   path('insertTask',views.insertTask),
   path('loginTask',views.loginTask),
   path('db',views.db),
       
]
