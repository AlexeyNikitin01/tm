# Generated by Django 4.0.5 on 2022-07-04 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RepairOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('surname', models.CharField(blank=True, max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('date_order', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-date_order'],
            },
        ),
    ]
