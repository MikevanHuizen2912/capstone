# Generated by Django 4.1.7 on 2023-04-03 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_alter_transaction_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='send_transaction', to='bank.bankaccount'),
        ),
    ]
