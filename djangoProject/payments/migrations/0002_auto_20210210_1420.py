# Generated by Django 3.1.6 on 2021-02-10 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyPaymentModel',
            new_name='Payment',
        ),
    ]
