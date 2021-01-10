# Generated by Django 3.1.5 on 2021-01-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_id', models.CharField(max_length=100)),
                ('bookmarked', models.BooleanField()),
            ],
            options={
                'db_table': 'bookmarks',
            },
        ),
    ]
