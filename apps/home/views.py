from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render
import qrcode
from django.core.files import File
import os
from .forms import *
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework import generics

@login_required(login_url="/login/")
def index(request):

    context = {

    }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def generator(request):
    context = {
        'url': None,
        'segment': 'generate'
    }
    return render(request, 'home/generator_qr.html', context)


def file_input_view(request):
    if request.method == 'POST':
        form = CreatePdfForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            try:
                docs = DocsObjects.objects.filter(id=form.cleaned_data['url']).first()
                if docs:
                    docs.file = uploaded_file
                    docs.date = form.cleaned_data['date']
                    docs.who_signed = form.cleaned_data['who_signed']
                    docs.document_address = form.cleaned_data['document_address']
                    docs.signatory_position = form.cleaned_data['signatory_position']
                    docs.signatory_workplace = form.cleaned_data['signatory_workplace']
                    docs.performer = form.cleaned_data['performer']
                    docs.performer_position = form.cleaned_data['performer_position']
                    docs.performer_workplace = form.cleaned_data['performer_workplace']
                    docs.start_ERI = form.cleaned_data['start_ERI']
                    docs.end_ERI = form.cleaned_data['end_ERI']
                    docs.given_by_ERI = form.cleaned_data['given_by_ERI']
                    docs.save()
            except:
                pass
        form = CreatePdfForm()
    else:
        form = CreatePdfForm()

    return render(request, 'home/add_file.html', {'form': form, 'segment': 'add_file'})


def generate_qr_code(request):
    if request.method == "POST":
        docs = DocsObjects.objects.create()
        url = f'https://check.ijra.uz/d/{docs.id}'
        q = qrcode.make(url)
        q.save('qrcode.png')
        with open('qrcode.png', 'rb') as img_file:
            docs.qrcode.save(os.path.basename('qrcode.png'), File(img_file))
            docs.save()
        context = {
            'url': docs.id,
            'segment': 'generate',
            'docs': docs
        }
        return render(request, 'home/generator_qr.html', context)
    else:
        context = {
            'url': None,
            'segment': 'generate'
        }
        return render(request, 'home/generator_qr.html', context)


def get_file_guid(request, id):
    if request.method == 'POST':
        form = GetPinForm(request.POST)
        if form.is_valid():
            try:
                docs = DocsObjects.objects.filter(id=id).first()
                if docs and docs.code == form.cleaned_data['code']:
                    file_field = docs.file
                    if file_field:
                        file_name = file_field.name.split('/')[-1]
                        response = FileResponse(file_field, filename=file_name)
                        return response
            except:
                pass
        form = GetPinForm()
    else:
        form = GetPinForm()

    return render(request, 'home/get_file.html', {'form': form})


def test_ijro(request, variable):
    context = {
        'object': None
    }
    obj = DocsObjects.objects.filter(id=variable).first()
    if obj:
        month_names = {
            1: "янв", 2: "фев", 3: "мар", 4: "апр", 5: "май", 6: "июн",
            7: "июл", 8: "авг", 9: "сен", 10: "окт", 11: "ноя", 12: "дек"
        }
        context = {
            'object': obj,
            'date': f"{obj.date.day:02d} {month_names[obj.date.month]} {obj.date.year}",
            'start_ERI': f"{obj.start_ERI.day:02d} {month_names[obj.start_ERI.month]} {obj.start_ERI.year}",
            'end_ERI': f"{obj.end_ERI.day:02d} {month_names[obj.end_ERI.month]} {obj.end_ERI.year}",
        }

    html_template = loader.get_template('home/check_test.html')
    return HttpResponse(html_template.render(context, request))


class DocsSerializer(ModelSerializer):

    class Meta:
        model = DocsObjects
        fields = "__all__"


class DocumentCheckView(generics.ListAPIView):
    serializer_class = DocsSerializer
    queryset = DocsObjects.objects.all()

    def list(self, request, *args, **kwargs):
        docs_id = request.GET.get('docs_id') if request.GET.get('docs_id') else ""
        document = DocsObjects.objects.filter(id=docs_id).first()
        data = []
        if document:
            serializer = self.get_serializer(document, many=True)
            data = serializer.data
        return Response(data)
