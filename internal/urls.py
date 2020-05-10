from django.urls import path

from web import views

urlpatterns = [
    path('list-person/', views.listperson, name='list-person'),
]
