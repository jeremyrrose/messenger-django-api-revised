# Generated by Django 3.1.1 on 2020-10-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_msg', '0014_auto_20200921_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.CharField(max_length=800, null=True),
        ),
    ]