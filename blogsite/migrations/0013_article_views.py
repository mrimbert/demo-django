# Generated by Django 5.0.1 on 2024-02-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0012_article_slug_page_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
