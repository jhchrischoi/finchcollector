# Generated by Django 4.2.1 on 2023-05-09 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('population', models.CharField(max_length=100)),
                ('habitat', models.CharField(max_length=100)),
                ('trend', models.CharField(max_length=100)),
            ],
        ),
    ]
