# Generated by Django 3.2.5 on 2021-07-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=6, unique=True)),
                ('password', models.CharField(max_length=6, unique=True)),
            ],
        ),
    ]
