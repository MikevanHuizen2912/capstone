# Generated by Django 4.1.7 on 2023-04-08 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_alter_transaction_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='holder_name',
            field=models.CharField(default='testvalue', max_length=150),
            preserve_default=False,
        ),
    ]