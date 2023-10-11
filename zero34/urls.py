from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PictureView.as_view(), name='home'),
    path('about/<int:pk>/', AboutPicture.as_view(), name='about'),
    path('create/', CreatePicture.as_view(), name='create'),
    path('delete/<int:pk>/', DeletePicture.as_view(), name='delete'),
    path('artist/', ArtistView.as_view(), name='artist'),
    path('create_artist/', CreateArtist.as_view(), name='create_artist')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
