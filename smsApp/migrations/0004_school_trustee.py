# Generated by Django 5.0.6 on 2024-06-12 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsApp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=200)),
                ('Level', models.CharField(choices=[('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Both Primary&Secondary', 'Both Primary&Secondary'), ('Tertiary', 'Tertiary')], max_length=100)),
                ('Location', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu'), ('Mombasa', 'Mombasa'), ('Marsabit', 'Marsabit'), ('Kajiado', 'Kajiado'), ('Lamu', 'Lamu'), ('Kilifi', 'Kilifi'), ('Kakamega', 'Kakamega'), ('Kisii', 'Kisii'), ('Turkana', 'Turkana')], max_length=100)),
                ('phone', models.IntegerField()),
                ('Student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsApp.student')),
            ],
        ),
        migrations.CreateModel(
            name='Trustee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=20)),
                ('Student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='smsApp.student')),
            ],
        ),
    ]
