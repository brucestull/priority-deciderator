from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser
from config.settings.common import THE_SITE_NAME


USER_DETAIL_PAGE_TITLE = "Dashboard"


class CustomLoginView(LoginView):
    """
    Override the default login view. This will allow us to add the site name to the context and then display it on the page.
    """

    def get_context_data(self, **kwargs):
        """
        Get the parent `context` and add the site name to the it.
        """
        context = super().get_context_data(**kwargs)
        context["the_site_name"] = THE_SITE_NAME
        return context


class SignUpView(CreateView):
    """
    View for user to create a new account.
    """

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def get_context_data(self, **kwargs):
        """
        Add the site name to the context.
        """
        context = super().get_context_data(**kwargs)
        context["the_site_name"] = THE_SITE_NAME
        return context


class UserUpdateView(UpdateView):
    """
    View for user to update an existing account.
    """

    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("login")
    template_name = "registration/update.html"

    def get_context_data(self, **kwargs):
        """
        Add the site name to the context.
        """
        context = super().get_context_data(**kwargs)
        context["the_site_name"] = THE_SITE_NAME
        return context


class UserDetailView(DetailView):
    """
    View for a user's dashboard page.
    """

    model = CustomUser

    def get_context_data(self, **kwargs):
        """
        Add the site name to the context.
        """
        context = super().get_context_data(**kwargs)
        context["the_site_name"] = THE_SITE_NAME
        context["page_title"] = USER_DETAIL_PAGE_TITLE
        return context

    # template_name = "accounts/user_detail.html"
    # context_object_name = "user"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["tasks"] = self.object.tasks.all()
    #     context["subtasks"] = self.object.subtasks.all()
    #     return context

    def get_object(self):
        return self.request.user
