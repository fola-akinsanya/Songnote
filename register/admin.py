from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
	list_display = ["user", "User_type", "city_of_residence"]

admin.site.register(Profile,ProfileAdmin)


