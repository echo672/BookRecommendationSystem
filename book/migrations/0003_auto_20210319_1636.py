# Generated by Django 3.1.7 on 2021-03-19 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210319_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=6),
        ),
    ]