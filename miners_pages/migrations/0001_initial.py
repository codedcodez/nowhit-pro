# Generated by Django 2.2.6 on 2019-11-06 10:14

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('miners_account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_address', models.CharField(max_length=200, verbose_name='BTC Address')),
                ('btc_address_link', models.URLField(max_length=500, verbose_name='BTC Address Link')),
                ('amount', models.DecimalField(decimal_places=8, max_digits=20)),
                ('date_updated', models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Date Updated')),
            ],
        ),
        migrations.CreateModel(
            name='SilverPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_address', models.CharField(max_length=200, verbose_name='BTC Address')),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(4), django.core.validators.MaxValueValidator(7)], verbose_name='BTC Amount to Mine')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miners_account.UserProfile')),
                ('investor_check', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlatinumPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_address', models.CharField(max_length=200, verbose_name='BTC Address')),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(20)], verbose_name='BTC Amount to Mine')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miners_account.UserProfile')),
                ('investor_check', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GoldPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_address', models.CharField(max_length=200, verbose_name='BTC Address')),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(8), django.core.validators.MaxValueValidator(15)], verbose_name='BTC Amount to Mine')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miners_account.UserProfile')),
                ('investor_check', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BronzePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_address', models.CharField(max_length=200, verbose_name='BTC Address')),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)], verbose_name='BTC Amount to Mine')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miners_account.UserProfile')),
                ('investor_check', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
