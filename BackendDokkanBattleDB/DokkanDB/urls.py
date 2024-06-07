from django.conf.urls import url
from DokkanDB import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^cards$',views.CardsApi)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
