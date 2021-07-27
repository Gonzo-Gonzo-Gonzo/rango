from django.urls import path
from rango import views

app_name:'rango'

urlpatterns = [
    path('index',views.index,name='index'),
    path('gonzotriesathing',views.index,name="gonzo'sThing"),
    path ('about',views.about,name='about'),
]

