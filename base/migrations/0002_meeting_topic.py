# Generated by Django 5.0.6 on 2024-07-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='topic',
            field=models.ManyToManyField(blank=True, related_name='Topic', to='base.topic'),
        ),
    ]
