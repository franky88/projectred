from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RedUser(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	profile_pic = models.ImageField(null=True, blank=True, verbose_name="profile picture")
	contact =models.CharField(max_length=20, null=True, blank=True)
	def __str__(self):
		return self.user.get_full_name()