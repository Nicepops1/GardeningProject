# Generated by Django 4.0.4 on 2022-07-15 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_alter_coment_photo_alter_post_photo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cordmark',
        ),
        migrations.CreateModel(
            name='Coordinat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cord_X', models.IntegerField(default=37.64)),
                ('cord_Y', models.IntegerField(default=55.76)),
                ('mesto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forum.post')),
            ],
        ),
    ]
