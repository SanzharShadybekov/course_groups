# Generated by Django 4.2.1 on 2023-06-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(related_name='john', to='group.student'),
        ),
    ]
