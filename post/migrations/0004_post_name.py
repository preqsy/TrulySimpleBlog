# Generated by Django 4.0.3 on 2022-03-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]