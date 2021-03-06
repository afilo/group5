# Generated by Django 4.0.5 on 2022-06-17 03:28

import database.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('employee_id', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('state', models.CharField(choices=[('AC', 'Accepted'), ('PE', 'Pending'), ('CA', 'Cancelled'), ('DR', 'Drafted')], max_length=2)),
                ('cart', djongo.models.fields.ArrayField(model_container=database.models.Cart)),
                ('total', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('box_quantity', models.IntegerField()),
                ('box_weight', models.IntegerField()),
                ('box_dimensions', models.CharField(default='-', max_length=100)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='custom_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_employee', models.BooleanField(default=False)),
                ('is_client', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
