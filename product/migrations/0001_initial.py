# Generated by Django 5.1.4 on 2024-12-29 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('quant', models.IntegerField(default=0)),
            ],
        ),
    ]