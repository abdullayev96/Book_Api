# Generated by Django 4.2.4 on 2023-09-14 10:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_alter_author_book_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book_number',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Kitoblar soni '),
        ),
    ]
