# Generated by Django 4.0.2 on 2022-02-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JFLaughs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(max_length=100000)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
