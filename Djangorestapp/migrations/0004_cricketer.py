# Generated by Django 4.1.5 on 2023-01-27 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Djangorestapp', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cricketer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('role', models.CharField(max_length=64)),
                ('jersyno', models.IntegerField()),
                ('favshort', models.CharField(max_length=64)),
            ],
        ),
    ]