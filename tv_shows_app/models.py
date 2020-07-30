from django.db import models
from datetime import date
import re


# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors['email'] = "Invalid email address!"
        # return errors
        if len(postData['title']) < 2:
            errors["title"] = "Title name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        # if (postData["release_date"]) > datetime.date.today():
        #     errors["release_date"] = "Date must be in the past"
        if len(postData['description']) < 10:
            errors["description"] = "Description should be at least 10 characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
