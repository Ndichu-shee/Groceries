# Generated by Django 3.1 on 2020-09-02 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=6)),
                ('phone_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('id_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('supplier_price', models.DecimalField(decimal_places=4, max_digits=20)),
                ('selling_price', models.DecimalField(decimal_places=4, max_digits=20)),
                ('number_in_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=30)),
                ('notes', models.TextField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='grocery.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=6)),
                ('phone_number', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('id_number', models.IntegerField()),
                ('profile_picture', models.ImageField(upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('date_palced', models.DateTimeField()),
                ('status', models.CharField(max_length=30)),
                ('delivery_time', models.DateTimeField()),
                ('order_price', models.DecimalField(decimal_places=4, max_digits=20)),
                ('shipping_cost', models.DecimalField(decimal_places=4, max_digits=20)),
                ('totalPrice', models.DecimalField(decimal_places=4, max_digits=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.customer')),
            ],
        ),
    ]
