# Generated by Django 4.1.7 on 2023-03-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_app', '0002_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(),
        ),
    ]
