# Generated by Django 3.2 on 2022-04-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredians', models.TextField(max_length=200)),
                ('process', models.TextField(max_length=200)),
            ],
        ),
    ]
