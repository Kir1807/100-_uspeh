from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.gl),
    
    path('admin', views.admin),
    path('login', views.login, name='form'),
    path('logout', views.logout, name='form'),
    path('profile', views.profile),
    path('results', views.results),
    path('consultation', views.consultation),

    # path('<pk>/', views.quiz_view),
    # path('<pk>/data/', views.quiz_data_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

