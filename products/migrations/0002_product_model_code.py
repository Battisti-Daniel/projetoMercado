# Generated by Django 4.2 on 2023-04-27 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product_model",
            name="code",
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
    ]
