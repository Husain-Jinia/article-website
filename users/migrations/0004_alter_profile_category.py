# Generated by Django 4.0.3 on 2022-04-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
        ('users', '0003_profile_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='category',
            field=models.ManyToManyField(related_name='profile', to='article.category'),
        ),
    ]