# Generated by Django 4.2.8 on 2023-12-19 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='placeofsupply',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
