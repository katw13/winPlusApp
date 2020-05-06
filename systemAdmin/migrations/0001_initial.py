# Generated by Django 2.1.1 on 2020-05-05 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('cost', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenNumber', models.CharField(max_length=40)),
                ('winAmount', models.CharField(max_length=40)),
                ('winActivation', models.CharField(max_length=40)),
                ('currentInUse', models.BooleanField(blank=True, null=True)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systemAdmin.Package')),
            ],
        ),
    ]