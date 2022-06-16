# Generated by Django 4.0.3 on 2022-06-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bannerssettings',
            old_name='is_active_news_and_promotion',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='bannerssettings',
            old_name='speed_news_and_promotion',
            new_name='speed',
        ),
        migrations.RemoveField(
            model_name='bannerssettings',
            name='is_active_top_banner',
        ),
        migrations.RemoveField(
            model_name='bannerssettings',
            name='speed_top_banner',
        ),
        migrations.AddField(
            model_name='bannerssettings',
            name='settings_for',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]