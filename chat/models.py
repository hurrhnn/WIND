from django.db import models


# Create your models here.
class UserInfo(models.Model):
    UserName = models.CharField(max_length=10, null=False, blank=False, verbose_name='Name')
    UserId = models.EmailField(max_length=50, null=False, blank=False, verbose_name='ID')
    UserPassword = models.CharField(max_length=24, null=False, blank=False, verbose_name='Password')

    UserStudentId = models.PositiveSmallIntegerField(null=False, blank=False, verbose_name='Student ID')
    DepartmentChoices = (
        ("information", "정보보호과"), ("software", "소프트웨어과"), ("business", "IT경영학과"), ("design", "콘텐츠디자인과"))
    UserDepartment = models.CharField(choices=DepartmentChoices, max_length=11, null=False, blank=False,
                                      verbose_name='Department')
    UserProfile = models.ImageField(width_field=64, height_field=64, null=True, blank=True,
                                    verbose_name='Profile Image')

    UserStatus = models.BooleanField(null=False, blank=False, verbose_name="I'm sim sim")
    UserFavorite = models.CharField(max_length=2048, null=True, blank=True, verbose_name='Favorite')

    def __str__(self):
        return self.UserName

    class Meta:
        db_table = 'userinfo'
        ordering = ['UserId']
