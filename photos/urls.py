from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('', views.photos, name='photos'),
    url('search/', views.search_results, name='search_results'),
    url('location/(<location_name>\)/', views.get_image_by_location, name='location'),
]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)