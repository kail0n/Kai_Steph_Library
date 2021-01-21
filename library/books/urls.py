from django.urls import path
from . import views
from .views import homepage, show

urlpatterns = [

    path("", homepage),

    # path("", views.home, name='books-home'),
    path("books/<int:book_id>/", show, name='books-show')
]