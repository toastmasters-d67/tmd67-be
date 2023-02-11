# Generated by Django 4.1.5 on 2023-02-10 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ac", "0004_alter_paymentrecord_merchant_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="paymentrecord",
            old_name="due_date",
            new_name="due_time",
        ),
        migrations.RemoveField(
            model_name="paymentrecord",
            name="is_paid",
        ),
        migrations.AddField(
            model_name="paymentrecord",
            name="message",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="paymentrecord",
            name="result",
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name="paymentrecord",
            name="status",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]