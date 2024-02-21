from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile_register/', Profile_register.as_view(), name='book-list'),
    path('profile_register/<int:pk>/', Profile_registerUpdateDeleteView.as_view(), name='book-detail'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)