from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('autorize.urls')),
    path('', include('quizes.urls', namespace='quizes')),
    re_path(r'^accounts/', include('allauth.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
