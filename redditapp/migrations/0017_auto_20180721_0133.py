# Generated by Django 2.0.5 on 2018-07-20 20:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('redditapp', '0016_auto_20180721_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='profile',
            unique_together={('username',)},
        ),
    ]
