

from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views 


urlpatterns = [
				path('', views.signup, name='blog'),
] 


