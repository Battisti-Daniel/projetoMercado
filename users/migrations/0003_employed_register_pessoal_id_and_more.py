# Generated by Django 4.2 on 2023-04-29 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_employed_register_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="employed_register",
            name="pessoal_id",
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="employed_register",
            name="register_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
