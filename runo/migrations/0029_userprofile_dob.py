# Generated by Django 3.2 on 2021-08-05 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runo', '0028_alter_message_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]
