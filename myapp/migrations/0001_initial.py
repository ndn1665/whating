# Generated by Django 4.2.3 on 2023-08-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peoplenum', models.IntegerField(max_length=4)),
            ],
        ),
    ]
