from django.urls import path

from . import views

urlpatterns = [
    path("get-repo-structures", views.get_repo_structures, name="get_repo_structures"),
    path("repo-structure", views.repostructure, name="repostructure")
]