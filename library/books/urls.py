from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import homepage, show
from users import views as user_views

urlpatterns = [

    path("", homepage),

    # path("", views.home, name='books-home'),
    path("books/<int:book_id>/", show, name='books-show'),

    path('signup/', user_views.signup, name='signup')
]