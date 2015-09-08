from django.db import models


class User(models.Model):
	firstname = models.CharField(max_length=20, null=False)
	lastname = models.CharField(max_length=20, null=False)
	email = models.CharField(max_length=50, null=False)
	username = models.CharField(max_length=20, unique= True, null=False)
	password = models.CharField(max_length=50, null=False)