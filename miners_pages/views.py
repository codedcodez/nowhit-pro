from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from miners_account.models import UserProfile
from .forms import (BronzePackageForm, SilverPackageForm, GoldPackageForm, PlatinumPackageForm)
from .models import Transaction


def index(request):

    return render(request, 'miners_pages/index.html', {})

@login_required(login_url='login')
def create_bronze_package(request):

    if request.method == 'POST':
        bronze_form = BronzePackageForm(data=request.POST)

        if bronze_form.is_valid():
            form = bronze_form.save(commit=False)
            form_check = UserProfile.objects.get(user=request.user)
            form.investor = form_check
            form.save()

            return redirect('miners_pages:bronze_final')

    else:
        bronze_form = BronzePackageForm()

    context = {
        'bronze_form': bronze_form
    }

    return render(request, 'miners_pages/bronze.html', context)



@login_required(login_url='login')
def create_silver_package(request):

    if request.method == 'POST':
        silver_form = SilverPackageForm(data=request.POST)

        if silver_form.is_valid():
            form = silver_form.save(commit=False)
            form_check = UserProfile.objects.get(user=request.user)
            form.investor = form_check
            form.save()

            return redirect('miners_pages:silver_final')

    else:
        silver_form = SilverPackageForm()

    context = {
        'silver_form': silver_form
    }

    return render(request, 'miners_pages/silver.html', context)



@login_required(login_url='login')
def create_gold_package(request):

    if request.method == 'POST':
        gold_form = GoldPackageForm(data=request.POST)

        if gold_form.is_valid():
            form = gold_form.save(commit=False)
            form_check = UserProfile.objects.get(user=request.user)
            form.investor = form_check
            form.save()

            return redirect('miners_pages:gold_final')

    else:
        gold_form = GoldPackageForm()

    context = {
        'gold_form': gold_form
    }

    return render(request, 'miners_pages/gold.html', context)



@login_required(login_url='login')
def create_platinum_package(request):

    if request.method == 'POST':
        platinum_form = PlatinumPackageForm(data=request.POST)

        if platinum_form.is_valid():
            form = platinum_form.save(commit=False)
            form_check = UserProfile.objects.get(user=request.user)
            form.investor = form_check
            form.save()

            return redirect('miners_pages:platinum_final')

    else:
        platinum_form = PlatinumPackageForm()

    context = {
        'platinum_form': platinum_form
    }

    return render(request, 'miners_pages/platinum.html', context)


class BronzeFinalView(TemplateView):

    template_name = 'miners_pages/bronze_final.html'


class SilverFinalView(TemplateView):

    template_name = 'miners_pages/silver_final.html'


class GoldFinalView(TemplateView):

    template_name = 'miners_pages/gold_final.html'


class PlatinumFinalView(TemplateView):

    template_name = 'miners_pages/platinum_final.html'


def display_transactions(request):

    transactions = Transaction.objects.all().order_by('-date_updated')

    context = {
        'transactions': transactions
    }

    return render(request, 'miners_pages/transactions.html', context)


class AboutView(TemplateView):
    template_name = 'miners_pages/about.html'


class FAQSView(TemplateView):
    template_name = 'miners_pages/faqs.html'


class TCView(TemplateView):
    template_name = 'miners_pages/tnc.html'
