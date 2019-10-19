from django.contrib import admin

from miners_account.models import UserProfile
from .models import (BronzePackage, SilverPackage, GoldPackage, PlatinumPackage, Transaction)

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('country', )


class BronzePackageAdmin(admin.ModelAdmin):
    list_display = ('btc_address', 'amount', 'investor')
    readonly_fields = ('investor_check',)


class SilverPackageAdmin(admin.ModelAdmin):
    list_display = ('btc_address', 'amount', 'investor')
    readonly_fields = ('investor_check',)


class GoldPackageAdmin(admin.ModelAdmin):
    list_display = ('btc_address', 'amount', 'investor')
    readonly_fields = ('investor_check',)


class PlatinumPackageAdmin(admin.ModelAdmin):
    list_display = ('btc_address', 'amount', 'investor')
    readonly_fields = ('investor_check',)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('btc_address', 'btc_address_link', 'amount', 'date_updated')



admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(BronzePackage, BronzePackageAdmin)
admin.site.register(SilverPackage, SilverPackageAdmin)
admin.site.register(GoldPackage, GoldPackageAdmin)
admin.site.register(PlatinumPackage, PlatinumPackageAdmin)
admin.site.register(Transaction, TransactionAdmin)
