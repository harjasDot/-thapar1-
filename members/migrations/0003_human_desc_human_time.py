# Generated by Django 4.1.1 on 2022-09-07 10:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_human_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='desc',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='human',
            name='time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
