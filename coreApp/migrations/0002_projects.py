# Generated by Django 4.2.6 on 2023-10-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('published', models.DateField()),
                ('lastUpdated', models.DateField()),
            ],
        ),
    ]