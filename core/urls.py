from django.contrib import admin
from django.urls import path, include  # add this
from .settings import *
from django.conf.urls.static import static
from apps.home.views import get_file_guid, test_ijro, DocumentCheckView, GetFileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.authentication.urls")),
    path("", include("apps.home.urls")),
    path('d/<str:variable>/', test_ijro, name='test-retrieve'),
    path('api/docs_objects', DocumentCheckView.as_view(), name='get-docs_objects'),
    path('api/get_file', GetFileView.as_view(), name='get-docs_file'),

]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
