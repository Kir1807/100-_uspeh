from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    QuizListView,
    quiz_view
)

app_name = 'quizes'

urlpatterns = [
    path('', QuizListView.as_view, name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
]  
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)