# Generated by Django 5.0.1 on 2024-02-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0010_alter_test_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image_illus',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='test',
            name='upload',
            field=models.FileField(upload_to='blogsite/static/blog/images '),
        ),
    ]
