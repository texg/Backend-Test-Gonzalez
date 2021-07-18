from django.db import models
from uuid import uuid4


# Create your models here.

class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4())
    title_menu = models.CharField(max_length=200)
    menu_date = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title_menu


class Option(models.Model):
    title_option = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return self.title_option


class Order(models.Model):
    email_worker = models.CharField(max_length=200)
    name_worker = models.CharField(max_length=200)
    option_selected = models.ForeignKey(Option, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date_selection = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order to {self.name_worker}: {self.option_selected}, {self.comment}"
