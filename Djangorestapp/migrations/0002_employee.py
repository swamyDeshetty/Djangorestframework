# Generated by Django 4.1.5 on 2023-01-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Djangorestapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpName', models.CharField(max_length=40)),
                ('Emprole', models.CharField(max_length=40)),
                ('EmpSal', models.IntegerField()),
            ],
        ),
    ]
