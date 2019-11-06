from django import forms
from .models import BronzePackage, SilverPackage, GoldPackage, PlatinumPackage


class BronzePackageForm(forms.ModelForm):

    class Meta():
        model = BronzePackage
        fields = ('btc_address', 'amount')

        widgets = {
            'btc_address': forms.TextInput(attrs={'placeholder': 'Enter your btc wallet to receive payment'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter from 1 to 3'}),
        }



class SilverPackageForm(forms.ModelForm):

    class Meta():
        model = SilverPackage
        fields = ('btc_address', 'amount')

        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter from 4 to 7'}),
        }




class GoldPackageForm(forms.ModelForm):

    class Meta():
        model = GoldPackage
        fields = ('btc_address', 'amount')

        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter from 8 to 15'}),
        }




class PlatinumPackageForm(forms.ModelForm):

    class Meta():
        model = PlatinumPackage
        fields = ('btc_address', 'amount')

        widgets = {
            'amount': forms.NumberInput(attrs={'placeholder': 'Enter from 16 to 20'}),
        }
