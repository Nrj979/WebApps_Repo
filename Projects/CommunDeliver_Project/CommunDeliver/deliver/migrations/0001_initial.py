# Generated by Django 4.2.7 on 2023-12-04 05:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("custid", models.AutoField(primary_key=True, serialize=False)),
                ("custname", models.CharField(max_length=100)),
                ("custmail", models.CharField(max_length=200)),
                ("custpassword", models.CharField(max_length=150)),
                ("custcontact", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="Partner",
            fields=[
                ("partnerid", models.AutoField(primary_key=True, serialize=False)),
                ("partnername", models.CharField(max_length=100)),
                ("partnermail", models.CharField(max_length=200)),
                ("partneridproof", models.CharField(max_length=100)),
                ("partneridno", models.CharField(max_length=30)),
                ("partnerpassword", models.CharField(max_length=150)),
                ("partnercontact", models.CharField(max_length=30)),
                ("partnervehicle", models.CharField(max_length=200)),
                ("partnervehicleno", models.CharField(max_length=50)),
            ],
        ),
    ]