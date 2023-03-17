from django.views.generic.list import ListView

from config.settings.common import THE_SITE_NAME
from deciderator.models import Task

TASK_LIST_PAGE_TITLE = "Task List"


class TaskListView(ListView):
    """
    List view for tasks.
    """

    model = Task
    # context_object_name = "tasks"

    def get_queryset(self):
        """
        Get the tasks for the current user.
        """
        return Task.objects.filter(owner=self.request.user).order_by("-special_order")

    def get_context_data(self, **kwargs):
        """
        Get the context data for the template.
        """
        context = super().get_context_data(**kwargs)
        context["the_site_name"] = THE_SITE_NAME
        context["page_title"] = TASK_LIST_PAGE_TITLE
        return context