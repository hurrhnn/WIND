# Generated by Django 3.1.3 on 2020-11-17 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('UserName', models.CharField(max_length=10, verbose_name='Name')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='ID')),
                ('UserStudentId', models.PositiveSmallIntegerField(verbose_name='Student ID')),
                ('UserDepartment', models.CharField(choices=[('information', '정보보호과'), ('software', '소프트웨어과'), ('business', 'IT경영학과'), ('design', '콘텐츠디자인과')], max_length=11, verbose_name='Department')),
                ('UserProfile', models.ImageField(default='default.jpg', upload_to='../media/', verbose_name='Profile Image')),
                ('UserStatus', models.BooleanField(blank=True, default=False, verbose_name="I'm board")),
                ('UserFavorite', models.CharField(blank=True, max_length=2048, verbose_name='Favorite')),
                ('UserChannels', models.CharField(blank=True, max_length=2147483647, verbose_name='Joined Servers')),
                ('code_number', models.CharField(max_length=2048, primary_key=True, serialize=False, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'userinfo',
                'ordering': ['email'],
            },
        ),
    ]