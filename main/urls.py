# main/urls.py

from django.urls import path
from .views import send_bulk_email_view

urlpatterns = [
    path('send_bulk_email/', send_bulk_email_view, name='send_bulk_email'),
]
