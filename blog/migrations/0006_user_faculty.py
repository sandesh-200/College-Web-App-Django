# Generated by Django 5.0.1 on 2024-02-02 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_user_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='faculty',
            field=models.CharField(default='', max_length=225),
        ),
    ]