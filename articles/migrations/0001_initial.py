# Generated by Django 5.1.4 on 2024-12-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('short_content', models.TextField()),
                ('long_content', models.TextField()),
                ('author', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
