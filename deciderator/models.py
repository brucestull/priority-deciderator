from django.db import models
from django.urls import reverse

from config.settings.common import AUTH_USER_MODEL


class Task(models.Model):
    """
    Model for a task.
    """

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name="tasks",
        on_delete=models.CASCADE,
    )
    description = models.CharField(
        max_length=255,
    )
    completed = models.BooleanField(
        default=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date created",
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="date updated",
    )

    def __str__(self):
        return self.description[:50]

    # def get_absolute_url(self):
    #     return reverse("tasks:detail", args=(self.pk,))

    class Meta:
        ordering = ["-created"]


class SubTask(models.Model):
    """
    Model for a subtask.
    """

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name="subtasks",
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        Task,
        related_name="subtasks",
        on_delete=models.CASCADE,
    )
    description = models.CharField(
        max_length=255,
    )
    completed = models.BooleanField(
        default=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date created",
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="date updated",
    )

    def __str__(self):
        return self.description[:50] + " - " + self.task.description[:50]

    # def get_absolute_url(self):
    #     return reverse("subtasks:detail", args=(self.pk,))

    class Meta:
        ordering = ["-created"]


class ImportantConcept(models.Model):
    """
    Model for an important concept.
    """

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name="important_concepts",
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        Task,
        related_name="important_concepts",
        on_delete=models.CASCADE,
    )
    description = models.CharField(
        max_length=255,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date created",
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name="date updated",
    )

    def __str__(self):
        return self.description[:50] + " - " + self.task.description[:50]

    # def get_absolute_url(self):
    #     return reverse("important_concepts:detail", args=(self.pk,))

    class Meta:
        ordering = ["-created"]
