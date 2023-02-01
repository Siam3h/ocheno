from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=200, default='null')
	summary = models.TextField(default='null')

	def __str__(self):
		return self.title