from django.contrib import admin
from django.urls import path
from Cursos.views import detal_curso, lis_curso, index
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('cursos/<int:id_curso>', detal_curso, name='datalhe'),
    path('lista/',lis_curso, name='lis_curso'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

