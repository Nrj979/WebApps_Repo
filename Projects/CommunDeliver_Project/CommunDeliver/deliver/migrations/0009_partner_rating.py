# Generated by Django 4.2.7 on 2023-12-16 04:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deliver", "0008_deliveryrequest_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="partner",
            name="rating",
            field=models.CharField(default="5", max_length=20),
        ),
    ]
