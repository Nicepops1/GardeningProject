# Generated by Django 4.0.4 on 2022-07-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_rename_category_citys_rename_category_post_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='adresmark',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='cordmark',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
