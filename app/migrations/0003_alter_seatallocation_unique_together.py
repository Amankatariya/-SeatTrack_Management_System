# Generated by Django 5.1 on 2024-08-10 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_seatallocation_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seatallocation',
            unique_together=set(),
        ),
    ]