# Generated by Django 3.2.6 on 2021-08-12 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userInput', '0011_alter_hangout_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hangout',
            name='group_id',
            field=models.IntegerField(default=777),
        ),
    ]
