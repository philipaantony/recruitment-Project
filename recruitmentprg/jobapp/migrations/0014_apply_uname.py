# Generated by Django 3.2 on 2022-03-04 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0013_auto_20220304_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='uname',
            field=models.CharField(default=0, max_length=25),
        ),
    ]
