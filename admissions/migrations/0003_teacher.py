# Generated by Django 4.2.3 on 2023-08-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0002_rename_contant_student_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('exp', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
    ]