# Generated by Django 3.2.6 on 2021-08-12 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userInput', '0002_budgets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hangout',
            old_name='number_submitted',
            new_name='group_size',
        ),
    ]