# Generated by Django 4.0.4 on 2023-01-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combat_app', '0006_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fighter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profile_img', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=300)),
                ('contact', models.EmailField(max_length=20)),
                ('date', models.IntegerField()),
                ('month', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=80)),
                ('town', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=80)),
                ('document', models.FileField(max_length=250, upload_to='new/')),
                ('password', models.CharField(max_length=50)),
                ('fight_name', models.CharField(max_length=100)),
                ('fight_weight', models.CharField(max_length=50)),
                ('wight_units', models.CharField(max_length=20)),
                ('fight_height', models.CharField(max_length=50)),
                ('height_units', models.CharField(max_length=20)),
                ('gym_name', models.CharField(max_length=100)),
            ],
        ),
    ]
