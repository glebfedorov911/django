# Generated by Django 4.1.7 on 2023-04-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0007_alter_category_options_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='Имя пользователя'),
        ),
    ]
