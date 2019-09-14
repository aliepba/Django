# Generated by Django 2.2.3 on 2019-08-29 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=65)),
                ('detail', models.TextField()),
                ('category', models.CharField(max_length=40)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='media/upload')),
            ],
        ),
    ]