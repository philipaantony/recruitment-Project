# Generated by Django 3.2 on 2022-02-25 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0004_alter_company_cemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uemail',
            field=models.EmailField(max_length=254, unique='true', verbose_name='User Email'),
        ),
    ]
