# Generated by Django 3.1.5 on 2021-02-15 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EVapp', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electriccarlist',
            name='number',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
