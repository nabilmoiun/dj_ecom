# Generated by Django 4.0 on 2022-02-08 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('featured', models.BooleanField(default=False)),
                ('logo', models.URLField(blank=True, null=True)),
                ('description', models.CharField(blank=True, default='No description available', max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('thumbnail', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('discount_in_percentage', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, default='No description available', null=True)),
                ('featured', models.BooleanField(default=False)),
                ('stock', models.PositiveIntegerField(default=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_products', to='product.category')),
            ],
            options={
                'verbose_name_plural': 'products',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='product.product')),
            ],
            options={
                'verbose_name_plural': 'productimages',
                'ordering': ['-created_date'],
            },
        ),
    ]
