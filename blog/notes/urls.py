from . import views
from django.urls import path

app_name = 'notes'
urlpatterns = [
	path("", views.index, name="index"),
	path("blog/<blog_id>", views.details, name="show-details"),
]
