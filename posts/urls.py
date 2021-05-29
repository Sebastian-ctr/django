from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_home, name="post_home"),
    path("<str:id>/", views.post_detail, name="post_details")
]