from django.contrib import admin
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import RobloxUser
UserBase = get_user_model()

# Admin Panel Site Config
admin.site.site_title = settings.SERVER_NAME
admin.site.site_header = "Django Administration"

# Register your models here.
admin.site.register(UserBase)
admin.site.register(RobloxUser)