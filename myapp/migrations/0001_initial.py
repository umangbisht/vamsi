# Generated by Django 3.0.7 on 2020-06-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_record', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'excel_data',
            },
        ),
    ]
