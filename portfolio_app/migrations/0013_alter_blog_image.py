# Generated by Django 5.0 on 2024-03-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0012_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=False, upload_to='upload'),
        ),
    ]
