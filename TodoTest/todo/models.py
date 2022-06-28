from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default='')

    class Meta:
        unique_together = ('title', 'user')

    def __str__(self):
        return self.title


class Todo(models.Model):
    todo_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.todo_name





