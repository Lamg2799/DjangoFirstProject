# Generated by Django 2.0.7 on 2018-08-06 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signupAndLogin', '0006_auto_20180806_0251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customusermodel',
            old_name='CustomUser',
            new_name='CustomUserModel',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='item',
            new_name='Itemuser',
        ),
    ]
