# Generated by Django 3.1.7 on 2021-03-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('book_rating', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('book_author', models.CharField(max_length=50, null=True)),
                ('book_isbm', models.CharField(max_length=200)),
                ('press_information', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='BookandUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_pk', models.CharField(max_length=200)),
                ('user_pk', models.CharField(max_length=200)),
                ('rate_book_by_user', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('book_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'book_rating_by_user',
                'verbose_name_plural': 'books_rating_by_users',
            },
        ),
    ]
