from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    sex = models.CharField(max_length=1, null=False)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class DemoContent(models.Model):
    content = models.CharField(max_length=200)


class Document(models.Model):
    user = models.OneToOneField(User)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


