# Generated by Django 4.0 on 2022-02-08 09:55

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('discount_in_percentage', models.PositiveIntegerField(default=0)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order_items', to='product.product')),
            ],
            options={
                'verbose_name_plural': 'OrderItems',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=150)),
                ('phone_number', models.CharField(max_length=11)),
                ('transaction_id', models.CharField(blank=True, max_length=60, null=True)),
                ('city', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zip_code', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('invoice_id', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(choices=[('Received', 'Received'), ('On the way', 'On the way'), ('Delivered', 'Delivered')], default='Received', max_length=15)),
                ('total', models.DecimalField(decimal_places=2, max_digits=21)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('order_items', models.ManyToManyField(to='order.OrderItem')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_orders', to='auth.user')),
            ],
            options={
                'verbose_name_plural': 'orders',
                'ordering': ['-created_date'],
            },
        ),
    ]
