from django.urls import path
from .views import *

urlpatterns = [
    path('', BlockPageView.as_view(), name='main'),
    path('block/<str:slug>/', BlockPageView.as_view(), name='page'),
    path('category/<str:slug>/', CategoryView.as_view(), name='category'),
    path('about/', SingleView.as_view(), name='about'),
    path('gallery/', ArchiveView.as_view(), name='archive'),
    path('contact/', ContactView.as_view(), name='contact'),
]




# tillo.2006
# 2006.tillo