# Generated by Django 4.2.6 on 2023-10-04 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0002_alter_userinfo_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
    ]