# Generated by Django 5.0.6 on 2024-06-22 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_createbookborrowedhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createbookreview',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]