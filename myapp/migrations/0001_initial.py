# Generated by Django 4.1.5 on 2023-01-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banda', models.CharField(max_length=50)),
                ('local', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('data', models.DateField()),
            ],
        ),
    ]