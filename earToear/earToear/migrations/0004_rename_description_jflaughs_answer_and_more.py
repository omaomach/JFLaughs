# Generated by Django 4.0.2 on 2022-02-24 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('earToear', '0003_jflaughs_name_alter_jflaughs_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jflaughs',
            old_name='description',
            new_name='Answer',
        ),
        migrations.RenameField(
            model_name='jflaughs',
            old_name='name',
            new_name='Joke',
        ),
    ]