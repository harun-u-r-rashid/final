# Generated by Django 5.0 on 2024-03-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0008_alter_projectreview_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectreview',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
