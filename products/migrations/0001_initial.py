# Generated by Django 5.2 on 2025-04-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(default='暂无商品描述')),
                ('stock', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'products',
            },
        ),
    ]
