# Generated by Django 5.0 on 2024-03-03 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_projectreview_account_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='projectreview',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='projectreview',
            name='account',
        ),
    ]
