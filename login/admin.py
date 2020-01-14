from django.contrib import admin

from login.models import User, ConfirmString

admin.site.register(User)
admin.site.register(ConfirmString)