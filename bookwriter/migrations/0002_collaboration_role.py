# Generated by Django 4.2.5 on 2023-09-24 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookwriter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaboration',
            name='role',
            field=models.CharField(choices=[('Author', 'Author'), ('Collaborator', 'Collaborator')], default='-', max_length=20),
        ),
    ]
