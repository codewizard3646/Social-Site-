# Generated by Django 3.1.3 on 2021-01-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0009_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
