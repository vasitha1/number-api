from django.urls import path
from .views import classify_number

urlpatterns = [
    path('classify-number/', classify_number),
]