from django.urls import path

from internal import views

urlpatterns = [
    path('list-person/', views.listperson, name='list-person'),
]
