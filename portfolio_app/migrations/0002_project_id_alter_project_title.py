# Generated by Django 5.0 on 2024-03-03 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='id',
            field=models.IntegerField(default=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]