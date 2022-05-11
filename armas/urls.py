from django.urls import path

from .views import ArmaAPIView, MunicaoAPIView

urlpatterns = [
    path('armas/', ArmaAPIView.as_view(), name='armas'),
    path('municao/', MunicaoAPIView.as_view(), name='municao')
]
