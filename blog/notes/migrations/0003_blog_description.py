# Generated by Django 4.0.5 on 2022-06-14 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_blog_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(default='No Description Available', max_length=500),
        ),
    ]