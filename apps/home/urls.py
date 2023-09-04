# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('generator/', views.generator, name='generator'),
    path('add_file/', views.file_input_view, name='add_file'),
    path('generatre_qr/', views.generate_qr_code, name='generate_qr'),
    path('test_ijro', views.test_ijro, name='test_ijro')
]

