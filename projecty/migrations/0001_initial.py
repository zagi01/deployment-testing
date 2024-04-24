# Generated by Django 5.0.2 on 2024-02-26 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailsFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('second_name', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('security_number', models.IntegerField(max_length=6)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='FirstTry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survay_question1', models.CharField(max_length=200)),
                ('survay_question2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SecondTry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_survay1', models.CharField(max_length=200)),
                ('second_survay2', models.CharField(max_length=200)),
            ],
        ),
    ]