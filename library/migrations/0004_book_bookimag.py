# Generated by Django 3.2.5 on 2021-07-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20210718_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='BookImag',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
