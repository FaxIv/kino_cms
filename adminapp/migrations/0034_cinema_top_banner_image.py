# Generated by Django 4.0.3 on 2022-05-11 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0033_alter_basesitepage_seo_keywords_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='top_banner_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
