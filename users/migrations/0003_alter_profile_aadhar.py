# Generated by Django 4.2 on 2023-04-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_aadhar_alter_profile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='aadhar',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]