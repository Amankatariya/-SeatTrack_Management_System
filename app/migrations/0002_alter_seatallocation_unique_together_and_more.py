# Generated by Django 5.1 on 2024-08-09 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seatallocation',
            unique_together={('student', 'seat_id')},
        ),
        migrations.RemoveField(
            model_name='seatallocation',
            name='end_date',
        ),
    ]