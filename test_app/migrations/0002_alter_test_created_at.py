# Generated by Django 3.2.6 on 2021-08-10 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]