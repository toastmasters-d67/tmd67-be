# Generated by Django 4.1.2 on 2023-02-15 15:37

import django_fsm
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ac", "0004_paymentrecord_merchant_order_no_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="state",
            field=django_fsm.FSMField(default="draft", max_length=50),
        ),
    ]
