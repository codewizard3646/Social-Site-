# Generated by Django 3.1.3 on 2021-02-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0011_auto_20210210_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='connection',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='follower',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]
