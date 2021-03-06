# Generated by Django 4.0.3 on 2022-04-09 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0016_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='basesitepage',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery'),
        ),
        migrations.AddField(
            model_name='cinema',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery'),
        ),
        migrations.AddField(
            model_name='hall',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery'),
        ),
        migrations.AddField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.gallery'),
        ),
        migrations.AddField(
            model_name='movie',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery'),
        ),
    ]
