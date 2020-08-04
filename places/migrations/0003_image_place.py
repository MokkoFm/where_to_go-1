# Generated by Django 3.0.8 on 2020-08-04 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Place', verbose_name='Место'),
        ),
    ]