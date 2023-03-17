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
        return (
            self.owner.username
            + " : "
            + self.description[:50]
            + " - pk: "
            + str(self.pk)
            + " - special_order: "
            + str(self.special_order)
        )

    # def get_absolute_url(self):
    #     return reverse("tasks:detail", args=(self.pk,))

    special_order = models.IntegerField(
        default=1,
    )

    # def get_next_special_order(self):
    #     """
    #     Get the next special order number.

    #     Special order is used to order the tasks in the list view.
    #     The next special order will be the the number of the users tasks + 1.
    #     """
    #     return Task.objects.filter(owner=self.owner).count() + 1

    # def save(self, *args, **kwargs):
    #     """
    #     Save the task.

    #     If the task is new, assign the next special order.
    #     """
    #     if not self.pk:
    #         self.special_order = self.get_next_special_order()
    #     super(Task, self).save(*args, **kwargs)

    # def sort_and_assign_special_order(self):
    #     """
    #     Sort the tasks by special order and assign the special order to each task.

    #     This method is called when a task is saved.
    #     """
    #     tasks = Task.objects.filter(owner=self.owner).order_by("-special_order")
    #     for i, task in enumerate(tasks):
    #         task.special_order = i + 1
    #         task.save()

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
