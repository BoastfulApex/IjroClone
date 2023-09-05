from django.contrib import admin
from django.urls import path, include  # add this
from .settings import *
from django.conf.urls.static import static
from apps.home.views import get_file_guid, test_ijro


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.authentication.urls")),
    path("", include("apps.home.urls")),
    path('d/<str:variable>/', test_ijro, name='test-retrieve'),

]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
