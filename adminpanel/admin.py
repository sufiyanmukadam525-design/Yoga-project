from django.contrib import admin

# Register your models here.
from yogaapp.models import RegisteredUser

@admin.register(RegisteredUser)
class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "user_type", "user")
    search_fields = ("username", "email")
