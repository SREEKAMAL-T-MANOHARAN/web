from . import views
from django.urls import path

app_name = 'members'
urlpatterns = [
	path("login/", views.login_user, name="login"),
]
