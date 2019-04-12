# blog/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200,verbose_name= ('First Name'), null=True, blank=True)
	last_name = models.CharField(max_length=200, verbose_name= ('Last Name'), null=True, blank=True)
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

	def __str__(self):
		return self.user.username