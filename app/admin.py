from django.contrib import admin

# Register your models here.

from user.models import User
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username',  'email',  'password',  'user_type',  'document',  'phone',  'level')
    search_fields = ('username', 'email')
    list_filter = ('id', 'user_type')