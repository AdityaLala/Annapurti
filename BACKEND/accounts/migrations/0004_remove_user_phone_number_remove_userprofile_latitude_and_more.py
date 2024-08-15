# Generated by Django 5.0 on 2024-05-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rating_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='longitude',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Organization'), (2, 'Donor')], null=True),
        ),
    ]
