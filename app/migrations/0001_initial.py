# Generated by Django 5.1.3 on 2024-12-20 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=100)),
                ('dept_No', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Employee_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Employee_name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('Employee_email', models.EmailField(max_length=100)),
                ('Employee_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comm', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('hiredate', models.DateField(auto_now=True)),
                ('mgr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.employee')),
            ],
        ),
    ]
