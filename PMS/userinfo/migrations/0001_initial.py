# Generated by Django 5.0 on 2023-12-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinput',
            fields=[
                ('Bhk', models.IntegerField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=30)),
                ('bathroom', models.IntegerField()),
                ('balcony', models.CharField(max_length=5)),
                ('playground', models.CharField(max_length=5)),
                ('landmark', models.CharField(max_length=50)),
                ('price_range', models.IntegerField()),
            ],
        ),
    ]