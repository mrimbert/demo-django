# Generated by Django 5.0.1 on 2024-02-01 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenu',
            name='contentTitle',
            field=models.CharField(default='Contenu test', max_length=200),
            preserve_default=False,
        ),
    ]
