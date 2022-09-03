# Generated by Django 4.1 on 2022-09-02 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_alter_size_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='title',
            field=models.CharField(choices=[('Family_Size', '1'), ('Hungry_Size', '2'), ('Big_Size', '3'), ('Middle_Size', '4'), ('Small_Size', '5')], max_length=20),
        ),
    ]