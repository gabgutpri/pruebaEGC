# Generated by Django 2.0 on 2021-01-05 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_yes_no_question',
            field=models.BooleanField(default=False),
        ),
    ]
