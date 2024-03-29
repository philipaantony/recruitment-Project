# Generated by Django 3.2 on 2022-03-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0012_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='cname',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AddField(
            model_name='apply',
            name='email',
            field=models.EmailField(default=0, max_length=254),
        ),
        migrations.AddField(
            model_name='apply',
            name='jobtitle',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AddField(
            model_name='apply',
            name='jobtype',
            field=models.CharField(default=0, max_length=25),
        ),
    ]
