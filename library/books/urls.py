from django.urls import path
from . import views

urlpatterns = [
    path('<id>/', views.show, name='books-show')
]