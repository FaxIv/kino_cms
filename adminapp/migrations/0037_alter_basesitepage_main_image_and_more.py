# Generated by Django 4.0.3 on 2022-05-18 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0036_alter_hall_vip_seats_config_alter_session_seats_busy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basesitepage',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='hall',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movie',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
