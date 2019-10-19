# Generated by Django 2.2.6 on 2019-10-15 20:39

from django.conf import settings
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
            name='SilverPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_address', models.CharField(max_length=30, verbose_name='BTC Address')),
                ('amount', models.PositiveIntegerField(verbose_name='BTC Amount to Generate')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miners_account.UserProfile')),
                ('investor_check', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlatinumPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_address', models.CharField(max_length=30, verbose_name='BTC Address')),
                ('amount', models.PositiveIntegerField(verbose_name='BTC Amount to Generate')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miners_account.UserProfile')),
                ('investor_check', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GoldPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_address', models.CharField(max_length=30, verbose_name='BTC Address')),
                ('amount', models.PositiveIntegerField(verbose_name='BTC Amount to Generate')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miners_account.UserProfile')),
                ('investor_check', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BronzePackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_address', models.CharField(max_length=30, verbose_name='BTC Address')),
                ('amount', models.PositiveIntegerField(verbose_name='BTC Amount to Generate')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miners_account.UserProfile')),
                ('investor_check', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
