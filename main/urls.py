from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('sell',views.sell,name='sell'),
    path('storage',views.storage,name='storage'),
    path('market',views.market,name='market'),
    path('services',views.services,name='services'),
]