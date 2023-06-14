from django.contrib import admin
from django.urls import path
from Cursos.views import infor, ali,api, index
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('informatica/', infor, name='informatica'),
    path('apicultura/',api, name='apicultura'),
    path('alimentos/',ali, name='alimentos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

