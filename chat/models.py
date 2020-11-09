from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class UserAccountManager(BaseUserManager):
    def create_user(self, UserId, UserPassword=None, **extra_fields):
        if not UserId:
            raise ValueError('Email must be set.')
        user = self.model(UserId = UserId, UserPassword = UserPassword, **extra_fields)
        user.set_password(UserPassword)
        user.save(using=self._db)
        return user

    def create_superuser(self, UserId, UserPassword, **extra_fields):
        superuser = self.create_user(UserId, UserPassword, **extra_fields)
        superuser.is_admin = True
        superuser.save(using=self._db)
        return superuser

    def get_by_natural_key(self, email_):
        return self.get(code_number=email_)


class UserInfo(AbstractBaseUser):
    is_anonymous = False
    is_authenticated = True

    objects = UserAccountManager()
    code_number = models.CharField(max_length=100, unique=True)

    REQUIRED_FIELDS = (
        'UserPassword', 'UserName', 'UserStudentId', 'UserDepartment', 'UserStatus', 'UserFavorite',
        'code_number')
    USERNAME_FIELD = 'UserId'

    UserName = models.CharField(max_length=10, null=False, blank=False, verbose_name='Name')
    UserId = models.EmailField(max_length=50, null=False, blank=False, verbose_name='ID', unique=True)
    UserPassword = models.CharField(max_length=24, null=False, blank=False, verbose_name='Password')

    UserStudentId = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Student ID')
    UserDepartment = models.CharField(
        choices=(("information", "정보보호과"), ("software", "소프트웨어과"), ("business", "IT경영학과"), ("design", "콘텐츠디자인과")),
        max_length=11, null=False, blank=False,
        verbose_name='Department')
    UserProfile = models.ImageField(null=True, blank=True, verbose_name='Profile Image')

    UserStatus = models.BooleanField(null=False, blank=False, verbose_name="I'm board")
    UserFavorite = models.CharField(max_length=2048, null=True, blank=True, verbose_name='Favorite')

    def __str__(self):
        return self.UserName

    #def set_password(*args, **kwargs):
    #    print(args, kwargs)

    class Meta:
        db_table = 'userinfo'
        ordering = ['UserId']
