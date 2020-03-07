# Generated by Django 2.2.8 on 2020-03-07 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CareerGuidance', '0004_auto_20200307_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aptitude_Test',
            fields=[
                ('Question_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Question', models.CharField(default='null', max_length=100)),
                ('Option_1', models.CharField(default='null', max_length=100)),
                ('Option_2', models.CharField(default='null', max_length=100)),
                ('Option_3', models.CharField(default='null', max_length=100)),
                ('Option_4', models.CharField(default='null', max_length=100)),
                ('Answer', models.CharField(default='null', max_length=100)),
            ],
        ),
    ]
