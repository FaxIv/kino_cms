# Generated by Django 4.0.3 on 2022-04-05 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_cinema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('seo_url', models.URLField()),
                ('seo_title', models.CharField(max_length=50)),
                ('seo_keywords', models.CharField(max_length=80)),
                ('seo_description', models.TextField()),
                ('date_created', models.DateField()),
                ('date_updated', models.DateField()),
                ('seats_config', models.CharField(max_length=50, verbose_name='Simple seats config')),
                ('vip_seats_config', models.CharField(max_length=50, verbose_name='VIP seats config')),
                ('flag_3d', models.BooleanField(verbose_name='3D')),
                ('flag_2d', models.BooleanField(verbose_name='2D')),
                ('flag_imax', models.BooleanField(verbose_name='IMAX')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.cinema')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery')),
            ],
            options={
                'verbose_name': 'Hall',
                'verbose_name_plural': 'Halls',
            },
        ),
    ]
