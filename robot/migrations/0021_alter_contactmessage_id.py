# Generated by Django 5.2 on 2025-06-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0020_alter_contactmessage_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
