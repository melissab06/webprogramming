# Generated by Django 2.1.5 on 2020-09-07 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('이름', models.CharField(max_length=50)),
                ('전화번호', models.CharField(max_length=20)),
                ('이메일', models.EmailField(max_length=254)),
                ('주소', models.CharField(max_length=100)),
                ('생년월일', models.DateField()),
            ],
        ),
    ]
