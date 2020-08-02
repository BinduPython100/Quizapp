from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', views.logout_view, name="logout"),
    path('quiz_ans', views.quiz_ans, name="quiz_ans")
]
