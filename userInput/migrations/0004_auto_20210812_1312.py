# Generated by Django 3.2.6 on 2021-08-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userInput', '0003_rename_number_submitted_hangout_group_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='hangout',
            name='number_submitted',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='hangout',
            name='budget_type',
            field=models.CharField(max_length=10),
        ),
    ]
