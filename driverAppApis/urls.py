from django.urls import path
from . import views
urlpatterns = [
    path('qrcode',views.qr_code,name='Qrcode'),
]