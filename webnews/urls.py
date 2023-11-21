from django.contrib import admin
from django.urls import path, include
from noticia.views import HomeTemplateView, RegistrationView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('noticias/', include('noticia.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration', RegistrationView.as_view(), name='registration'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)