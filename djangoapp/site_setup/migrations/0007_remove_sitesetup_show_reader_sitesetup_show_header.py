# Generated by Django 4.2.6 on 2023-10-24 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0006_alter_sitesetup_favicon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetup',
            name='show_reader',
        ),
        migrations.AddField(
            model_name='sitesetup',
            name='show_header',
            field=models.BooleanField(default=True),
        ),
    ]
