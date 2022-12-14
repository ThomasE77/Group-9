# Generated by Django 3.2.10 on 2022-11-29 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_post_no_of_downloads'),
    ]

    operations = [
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='no_of_downloads',
        ),
        migrations.AddField(
            model_name='profile',
            name='no_of_downloads',
            field=models.IntegerField(default=0),
        ),
    ]
