from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PictureView.as_view(), name='home'),
    path('about/<int:pk>/', AboutPicture.as_view(), name='about'),
    path('create/', CreatePicture.as_view(), name='create')
]