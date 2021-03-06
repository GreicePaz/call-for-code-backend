# Generated by Django 2.2.13 on 2020-07-30 21:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grantor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('notification', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'grantors',
            },
        ),
        migrations.CreateModel(
            name='Ong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('logo', models.TextField(null=True)),
                ('cnpj', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(14)])),
                ('cause', models.CharField(max_length=1024, null=True)),
                ('description', models.TextField(null=True)),
                ('cep', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=1024)),
                ('number', models.IntegerField()),
                ('complement', models.CharField(max_length=1024, null=True)),
                ('link', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('bank', models.CharField(default='caixa_economica_federal', max_length=50)),
                ('account', models.CharField(max_length=50, null=True)),
                ('agency', models.CharField(max_length=50, null=True)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ongs',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, null=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.TextField(null=True)),
                ('url', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('key', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_project',
            },
        ),
        migrations.CreateModel(
            name='NeedVoluntary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('form', models.CharField(default='online', max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Ong')),
            ],
            options={
                'db_table': 'needs_voluntary',
            },
        ),
        migrations.CreateModel(
            name='NeedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=1)),
                ('description', models.TextField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Ong')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Products')),
            ],
            options={
                'db_table': 'needs_product',
            },
        ),
        migrations.CreateModel(
            name='NeedBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('expiration', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image_pay', models.TextField(null=True)),
                ('active', models.BooleanField(default=True)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
                ('ong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Ong')),
            ],
            options={
                'db_table': 'needs_bill',
            },
        ),
        migrations.CreateModel(
            name='ContributionVoluntary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Grantor')),
                ('need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.NeedVoluntary')),
            ],
            options={
                'db_table': 'contributions_voluntary',
            },
        ),
        migrations.CreateModel(
            name='ContributionProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_id', models.CharField(max_length=1024)),
                ('grantor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Grantor')),
                ('need', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.NeedProduct')),
            ],
            options={
                'db_table': 'contributions_product',
            },
        ),
        migrations.CreateModel(
            name='ContributionAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_id', models.CharField(max_length=1024)),
                ('grantor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Grantor')),
                ('need', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.NeedBill')),
            ],
            options={
                'db_table': 'contributions_amount',
            },
        ),
    ]
