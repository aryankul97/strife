# Generated by Django 2.1.4 on 2019-02-28 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190227_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comp_ID', models.CharField(max_length=1000)),
                ('Can_ID', models.CharField(max_length=1000)),
                ('Marks', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'CanMarks',
            },
        ),
    ]