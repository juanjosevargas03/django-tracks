# Generated by Django 3.2.10 on 2021-12-11 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211210_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
