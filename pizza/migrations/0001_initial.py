# Generated by Django 4.1 on 2022-09-02 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping1', models.CharField(choices=[('Pesto', 'Pesto'), ('Tomatoes', 'Tomatoes'), ('Cheese', 'Cheese'), ('Pepperoni', 'Pepperoni'), ('Olive', 'Olive')], max_length=50)),
                ('topping2', models.CharField(choices=[('Pesto', 'Pesto'), ('Tomatoes', 'Tomatoes'), ('Cheese', 'Cheese'), ('Pepperoni', 'Pepperoni'), ('Olive', 'Olive')], max_length=50)),
                ('piece', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('size', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pizza.size', verbose_name='Size')),
            ],
        ),
    ]