from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Email must be set.')
        user = self.model(email=self.normalize_email(email), password=password, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        superuser = self.create_user(email, password, **kwargs)
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.save(using=self._db)
        return superuser

    def get_by_natural_key(self, email):
        return self.get(email=email)


class UserInfo(AbstractBaseUser, PermissionsMixin):
    DEP_ID_TO_NAME = {
        "information": "정보보호과",
        "software": "소프트웨어과",
        "business": "IT경영학과",
        "design": "콘텐츠디자인과"
    }

    objects = UserAccountManager()

    REQUIRED_FIELDS = ('UserName', 'UserStudentId', 'UserDepartment', 'UserStatus', 'UserFavorite', 'code_number')
    USERNAME_FIELD = 'email'

    UserName = models.CharField(max_length=10, null=False, blank=False, verbose_name='Name')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='ID', unique=True)

    UserStudentId = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Student ID')
    UserDepartment = models.CharField(
        choices=zip(DEP_ID_TO_NAME.keys(), DEP_ID_TO_NAME.values()),
        max_length=11, null=False, blank=False,
        verbose_name='Department')
    UserProfile = models.ImageField(null=False, upload_to='../media/', default='default.jpg',
                                    verbose_name='Profile Image')

    UserStatus = models.BooleanField(null=False, blank=True, verbose_name="I'm board", default=False)
    UserFavorite = models.CharField(max_length=2048, null=False, blank=True, verbose_name='Favorite')

    UserChannels = models.CharField(max_length=0x7fffffff, null=False, blank=True, verbose_name='Joined Servers')

    code_number = models.CharField(max_length=2048, primary_key=True, unique=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def get_dep(self):
        return zip(self.DEP_ID_TO_NAME.keys(), self.DEP_ID_TO_NAME.values())

    def get_status(self):
        return "checked" if self.UserStatus else ""

    def change_user_information(self, request):
        self.email = request.POST.get('email', None)
        self.UserStudentId = request.POST.get('student_id', None)
        self.UserDepartment = request.POST.get('department', None)
        self.UserFavorite = request.POST.get('favorite', None)
        status = request.POST.get('user_status', None)
        self.UserStatus = False if status is None else True

        self.save()

    def change_user_channels(self, operator, channel):
        if operator == '+':
            if channel not in self.UserChannels.split(","):
                if self.UserChannels:
                    self.UserChannels += "," + channel
                else:
                    self.UserChannels = channel
        elif operator == '-':
            user_channels = self.UserChannels.split(",")
            try:
                idx = user_channels.index(channel)
                del user_channels[idx]
                self.UserChannels = ",".join(user_channels)
            except ValueError:
                pass
        self.save(update_fields=['UserChannels'])

    class Meta:
        db_table = 'userinfo'
        ordering = ['email']
