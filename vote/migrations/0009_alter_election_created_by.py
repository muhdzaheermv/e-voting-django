# Generated by Django 4.2.7 on 2025-01-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0008_alter_election_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='created_by',
            field=models.CharField(max_length=20),
        ),
    ]
