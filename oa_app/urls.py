from django.urls import path

from oa_app import views


urlpatterns = [
    path('', views.index, name="index"),
    path('welcome.html', views.welcome, name="welcome"),
    path('login', views.log_in, name="login"),
    path('logout', views.log_out, name="logout"),
    path('login/handler/', views.login_handler, name="login_handler"),
]
