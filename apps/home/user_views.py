from django.http import HttpResponse
from rest_framework import generics
from django.http import FileResponse
from .models import DocsObjects


class FileRetrieveAPIView(generics.RetrieveAPIView):
    queryset = DocsObjects.objects.all()
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        file_field = instance.file

        if file_field:
            file_name = file_field.name.split('/')[-1]
            response = FileResponse(file_field, filename=file_name)
            return response
        else:
            return HttpResponse("File not found.", status=404)