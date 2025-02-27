# Generated by Django 4.1.7 on 2023-04-03 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorid', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('morningtoken', models.PositiveIntegerField(default=1)),
                ('afternoontoken', models.PositiveIntegerField(default=1)),
                ('eveninggtoken', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='bookedappointments',
            fields=[
                ('bookingid', models.AutoField(primary_key=True, serialize=False)),
                ('doctorid', models.PositiveIntegerField()),
                ('patientid', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('slot', models.CharField(max_length=100)),
                ('status', models.CharField(default='no action taken', max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('phone_number', models.IntegerField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9999999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{10}$')])),
                ('address', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Enter a valid Indian pincode.', regex='^[1-9][0-9]{5}$')])),
                ('age', models.PositiveIntegerField()),
                ('certificate', models.FileField(blank=True, upload_to='doctor_certificates')),
                ('experience', models.CharField(max_length=100)),
                ('isdelete', models.BooleanField(default=False)),
                ('hospitalid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9999999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{10}$')])),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Enter a valid Indian pincode.', regex='^[1-9][0-9]{5}$')])),
                ('description', models.CharField(max_length=100)),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('phone_number', models.IntegerField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9999999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{10}$')])),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Enter a valid Indian pincode.', regex='^[1-9][0-9]{5}$')])),
                ('description', models.CharField(max_length=100)),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
    ]
