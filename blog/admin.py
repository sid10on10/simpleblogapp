# blog/admin.py

from django.contrib import admin
from blog.models import UserProfileInfo, User

# Register your models here.
admin.site.register(UserProfileInfo)