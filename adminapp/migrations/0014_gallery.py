# Generated by Django 4.0.3 on 2022-04-09 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0013_remove_basesitepage_gallery_remove_cinema_gallery_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('gallery', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Gallery',
            },
        ),
    ]
