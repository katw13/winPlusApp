# Generated by Django 2.1.1 on 2020-05-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemAdmin', '0002_promotionoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='winActivation',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
