# Generated by Django 4.2 on 2023-04-30 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_cat', models.CharField(choices=[('Laptop', 'Laptop'), ('Accessories', 'Accessories'), ('Camera', 'Camera')], max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_desc', models.TextField()),
                ('product_price', models.PositiveSmallIntegerField()),
                ('product_image', models.ImageField(upload_to='product_image/')),
                ('product_stock', models.PositiveSmallIntegerField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
