# Generated by Django 4.0.3 on 2022-04-13 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0020_remove_basesitepage_gallery_remove_cinema_gallery_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Gallery',
            },
        ),
        migrations.RemoveField(
            model_name='basesitepage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='cinema',
            name='image',
        ),
        migrations.RemoveField(
            model_name='hall',
            name='image',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='image',
        ),
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
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery'),
        ),
        migrations.AddField(
            model_name='movie',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='adminapp.gallery'),
        ),
    ]