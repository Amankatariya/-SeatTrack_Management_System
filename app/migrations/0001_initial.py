# Generated by Django 5.1 on 2024-08-09 08:21

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_Date')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_Date')),
                ('seat_no', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_Date')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='app.classroom')),
                ('seat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.seat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SeatAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_Date')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.classroom')),
                ('seat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.seat')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_history', to='app.student')),
            ],
            options={
                'unique_together': {('student', 'seat_id', 'start_date')},
            },
        ),
    ]
