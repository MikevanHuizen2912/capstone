# Generated by Django 4.1.7 on 2023-04-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_remove_transaction_name_transaction_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
