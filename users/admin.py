from django.contrib import admin

from users.models import User, Habit

admin.site.register(User)

admin.site.register(Habit)