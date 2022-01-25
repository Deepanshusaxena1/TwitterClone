from django.contrib import admin

# Register your models here.
from accounts.models import Follow, User

admin.site.register(Follow)
admin.site.register(User)
