from django.contrib import admin
from django.urls import path

#import static and settings
from django.conf.urls.static import static
from django.conf import settings

#import event_page views
from event_page.views import home, like, like_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='homepage'),
    path('liked/', like_page, name='like_page'),
    path('like/<int:pk>', like, name='liked'),
]

#adding my media path and media roots to urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
