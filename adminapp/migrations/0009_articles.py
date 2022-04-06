# Generated by Django 4.0.3 on 2022-04-05 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_hall'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('basesitepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='adminapp.basesitepage')),
                ('video_url', models.URLField(verbose_name='Video')),
                ('date_publication', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'News and promotion',
                'verbose_name_plural': 'News and promotions',
            },
            bases=('adminapp.basesitepage',),
        ),
    ]