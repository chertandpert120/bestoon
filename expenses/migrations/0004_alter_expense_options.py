# Generated by Django 3.2.11 on 2022-02-16 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_auto_20220212_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'verbose_name': 'خرج', 'verbose_name_plural': 'خرج ها'},
        ),
    ]