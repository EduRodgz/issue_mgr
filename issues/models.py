from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    

class Issue(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.Textfield()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    assingee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee"
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )
    
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])