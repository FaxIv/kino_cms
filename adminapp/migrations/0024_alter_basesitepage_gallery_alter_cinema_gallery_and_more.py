# Generated by Django 4.0.3 on 2022-04-13 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0023_gallery_remove_basesitepage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basesitepage',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery'),
        ),
        migrations.AlterField(
            model_name='hall',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery'),
        ),
        migrations.AlterField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery'),
        ),
    ]
