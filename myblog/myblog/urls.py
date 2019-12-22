
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', include('contact.urls')),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('blog/', include('blog.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
	