# Generated by Django 2.1.7 on 2019-03-16 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20190316_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]