# Generated by Django 3.0.7 on 2020-07-11 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreport',
            name='initial_severity',
            field=models.CharField(choices=[(None, '---Select---'), ('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Extreme', 'Extreme')], max_length=255),
        ),
        migrations.AlterField(
            model_name='incidentreport',
            name='location',
            field=models.CharField(choices=[(None, '---Select---'), ('Corporate Headoffice', 'Corporate Headoffice'), ('Regional Suboffice', 'Regional Suboffice'), ('Branch Office', 'Branch Office')], max_length=255),
        ),
    ]
