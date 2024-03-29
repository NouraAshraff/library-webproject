# Generated by Django 3.2.5 on 2021-07-18 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookName', models.CharField(max_length=50)),
                ('AuthorName', models.CharField(max_length=50)),
                ('ISBN', models.CharField(max_length=20)),
                ('isBorrowed', models.BooleanField(default=0)),
                ('borrowingPeriod', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
