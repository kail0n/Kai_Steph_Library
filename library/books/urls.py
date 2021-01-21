from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import homepage, show, create
from users import views as user_views

urlpatterns = [

    path("", homepage, name='books-index'),

    # path("", views.home, name='books-home'),
    path("books/<int:book_id>/", show, name='books-show'),
     path("books/new/", create, name='books-create'),

    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout')
]