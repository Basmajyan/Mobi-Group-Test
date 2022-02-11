
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('test/<str:token>', views.finishedTest),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
