from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cats/<int:catid>/', categories),
    path('portal/', portal, name='portal'),
    path('create/', create, name='create'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('accounts/', include('accounts.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

