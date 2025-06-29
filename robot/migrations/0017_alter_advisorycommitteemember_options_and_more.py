# Generated by Django 5.2 on 2025-06-12 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0016_contactmessage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advisorycommitteemember',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='homepageimgslider',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['order']},
        ),
        migrations.RemoveField(
            model_name='advisorycommitteemember',
            name='sort_order',
        ),
        migrations.RemoveField(
            model_name='homepageimgslider',
            name='sort_order',
        ),
        migrations.RemoveField(
            model_name='person',
            name='sort_order',
        ),
        migrations.RemoveField(
            model_name='services',
            name='sort_order',
        ),
        migrations.AddField(
            model_name='advisorycommitteemember',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='homepageimgslider',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='services',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
