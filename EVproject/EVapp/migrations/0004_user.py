# Generated by Django 3.1.5 on 2021-02-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EVapp', '0003_answer_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=10)),
                ('Car_Model', models.CharField(max_length=30)),
            ],
        ),
    ]
