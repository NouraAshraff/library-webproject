# Generated by Django 3.2.5 on 2021-07-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_remove_book_bookimag'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='PublicationYear',
            field=models.DateField(null=True),
        ),
    ]