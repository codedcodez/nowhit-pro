from django.urls import path

from . import views

app_name = 'miners_pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('bronze-package', views.create_bronze_package, name='bronze_package'),
    path('silver-package', views.create_silver_package, name='silver_package'),
    path('gold-package', views.create_gold_package, name='gold_package'),
    path('platinum-package', views.create_platinum_package, name='platinum_package'),
    path('bronze-final', views.BronzeFinalView.as_view(), name='bronze_final'),
    path('silver-final', views.SilverFinalView.as_view(), name='silver_final'),
    path('gold-final', views.GoldFinalView.as_view(), name='gold_final'),
    path('platinum-final', views.PlatinumFinalView.as_view(), name='platinum_final'),
    path('transactions/', views.display_transactions, name='transactions'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('faqs/', views.FAQSView.as_view(), name='faqs'),
    path('tc/', views.TCView.as_view(), name='tc'),
]
