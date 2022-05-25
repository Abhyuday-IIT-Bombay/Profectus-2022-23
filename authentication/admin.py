from django.contrib import admin
from authentication.models import Account 
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Make_Resume , Apply
# from .models import file_upload

# Register your models here.

admin.site.register(Account)
admin.site.register(Make_Resume)
admin.site.register(Apply)
