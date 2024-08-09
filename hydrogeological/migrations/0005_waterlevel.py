# Generated by Django 5.0.6 on 2024-07-09 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydrogeological', '0004_alter_well_district_alter_well_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('I', models.FloatField(blank=True, null=True)),
                ('II', models.FloatField(blank=True, null=True)),
                ('III', models.FloatField(blank=True, null=True)),
                ('IV', models.FloatField(blank=True, null=True)),
                ('V', models.FloatField(blank=True, null=True)),
                ('VI', models.FloatField(blank=True, null=True)),
                ('VII', models.FloatField(blank=True, null=True)),
                ('VIII', models.FloatField(blank=True, null=True)),
                ('IX', models.FloatField(blank=True, null=True)),
                ('X', models.FloatField(blank=True, null=True)),
                ('XI', models.FloatField(blank=True, null=True)),
                ('XII', models.FloatField(blank=True, null=True)),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water_levels', to='hydrogeological.well')),
            ],
        ),
    ]