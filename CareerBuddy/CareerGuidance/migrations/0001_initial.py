# Generated by Django 3.0.2 on 2020-03-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('Job_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Job_Name', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
