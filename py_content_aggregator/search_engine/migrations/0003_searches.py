# Generated by Django 4.1.2 on 2022-10-15 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0002_search_sites_url_class_alter_search_sites_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Searches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchTerm', models.CharField(max_length=250)),
                ('date_time', models.DateTimeField()),
            ],
        ),
    ]
