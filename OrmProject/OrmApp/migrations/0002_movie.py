# Generated by Django 4.0.5 on 2022-11-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrmApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='images/')),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'tblmovies',
            },
        ),
    ]
