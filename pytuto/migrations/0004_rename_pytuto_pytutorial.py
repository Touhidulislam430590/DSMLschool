# Generated by Django 4.1.3 on 2023-10-05 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pytuto', '0003_rename_tutorial_pytuto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pytuto',
            new_name='pytutorial',
        ),
    ]