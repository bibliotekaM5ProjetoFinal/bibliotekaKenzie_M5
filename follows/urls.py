from django.urls import path
from . import views

urlpatterns = [
    path("follows/", views.FollowView.as_view()),
    path("follows/<int:pk>/", views.FollowDetailView.as_view()),
]
