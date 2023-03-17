from django.urls import path
from django.views.generic import TemplateView

from deciderator import views


app_name = "deciderator"

urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="home.html",
            extra_context={"the_site_name": "Deciderator"},
        ),
        name="deciderator-home",
    ),
    path(
        "tasks/",
        views.TaskListView.as_view(),
        name="task-list",
    ),
]