from django.contrib import admin
from django.contrib.auth import get_user_model


# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = (
        'UserName', 'email', 'password', 'UserStudentId', 'UserDepartment', 'UserStatus', 'UserFavorite')


admin.site.register(get_user_model(), UserInfoAdmin)
