# Generated by Django 4.2.2 on 2023-09-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('authores', models.CharField(max_length=40)),
                ('conteudo', models.CharField(max_length=500)),
                ('datacriacao', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
