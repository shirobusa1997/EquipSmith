# Generated by Django 2.2.5 on 2019-09-12 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='備品ID')),
                ('name', models.CharField(max_length=255, verbose_name='備品名')),
                ('equip_attribute', models.CharField(choices=[('book', '書籍'), ('depc', 'デスクトップPC'), ('lapc', 'ノートPC'), ('smph', 'スマートフォン')], max_length=2, verbose_name='種類')),
            ],
        ),
    ]
