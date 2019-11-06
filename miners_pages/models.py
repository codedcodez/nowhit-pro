from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

from miners_account.models import UserProfile


class BronzePackage(models.Model):
    btc_address = models.CharField(max_length=200, verbose_name='BTC Address')
    amount = models.PositiveIntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(3)], verbose_name='BTC Amount to Mine')
    investor_check = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    investor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.btc_address


class SilverPackage(models.Model):
    btc_address = models.CharField(max_length=200, verbose_name='BTC Address')
    amount = models.PositiveIntegerField(validators=[MinValueValidator(4),
                                       MaxValueValidator(7)], verbose_name='BTC Amount to Mine')
    investor_check = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    investor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.btc_address


class GoldPackage(models.Model):
    btc_address = models.CharField(max_length=200, verbose_name='BTC Address')
    amount = models.PositiveIntegerField(validators=[MinValueValidator(8),
                                       MaxValueValidator(15)], verbose_name='BTC Amount to Mine')
    investor_check = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    investor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.btc_address


class PlatinumPackage(models.Model):
    btc_address = models.CharField(max_length=200, verbose_name='BTC Address')
    amount = models.PositiveIntegerField(validators=[MinValueValidator(16),
                                       MaxValueValidator(20)], verbose_name='BTC Amount to Mine')
    investor_check = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    investor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.btc_address



class Transaction(models.Model):
    btc_address = models.CharField(max_length=200, verbose_name='BTC Address')
    btc_address_link = models.URLField(max_length=500, verbose_name='BTC Address Link')
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    date_updated = models.DateField(default=datetime.now, blank=True, verbose_name='Date Updated')

    def __str__(self):
        return self.btc_address
