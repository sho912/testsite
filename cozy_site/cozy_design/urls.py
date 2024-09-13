
from django.contrib import admin
from django.urls import path, include
from blog.views import frontpage
from .views import ContactFormView, ContactResultView
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('cozy-admin/', admin.site.urls),
    path('', frontpage),
    path('', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

