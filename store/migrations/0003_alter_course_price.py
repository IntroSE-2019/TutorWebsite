# Generated by Django 3.2.9 on 2021-11-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.BigIntegerField(),
        ),
    ]
