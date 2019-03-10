"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from demo import frontend_views, backend_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^echart/', include(('echart.urls','echart'))),
    re_path(r'^$', frontend_views.IndexView.as_view(), name='index'),
    re_path(r'^frontend_charts_list/$', frontend_views.FrontendEchartsTemplate.as_view(), name='frontend_demo'),
    re_path('^backend_charts_list/$', backend_views.BackendEChartsTemplate.as_view(), name='backend_demo'),

    re_path(r'multiple/Page/', backend_views.PageDemoView.as_view(), name='page_demo'),
    re_path(r'multiple/NamedCharts/', backend_views.NamedChartsView.as_view(), name='namedcharts_demo'),
    re_path(r'^demo/temperature/', backend_views.TemperatureEChartsView.as_view()),

    # Options Json for frontend views
    re_path(r'options/simpleBar/', frontend_views.SimpleBarView.as_view()),
    re_path(r'options/simpleKLine/', frontend_views.SimpleKLineView.as_view()),
    re_path(r'options/simpleMap/', frontend_views.SimpleMapView.as_view()),
    re_path(r'options/simplePie/', frontend_views.SimplePieView.as_view()),
    re_path(r'options/wordCloud/', frontend_views.WordCloudView.as_view()),
]
