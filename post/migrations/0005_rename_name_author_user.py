# Generated by Django 4.0.3 on 2022-03-23 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='user',
        ),
    ]
