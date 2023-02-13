# Generated by Django 4.1.5 on 2023-02-12 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ac", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="paymentrecord",
            name="due_time",
        ),
        migrations.RemoveField(
            model_name="ticket",
            name="ticket_product",
        ),
        migrations.AddField(
            model_name="ticket",
            name="ticket_products",
            field=models.ManyToManyField(
                related_name="tickets", to="ac.ticketproduct"
            ),
        ),
    ]
