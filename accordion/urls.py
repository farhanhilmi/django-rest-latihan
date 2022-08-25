import django
# from django.conf.urls import url
from django.urls import path, include
from .views import AccordionApiView, AccordionIdApiView

urlpatterns = [
    path('accordion', AccordionApiView.as_view()),
    path('accordion/<int:accordion_id>', AccordionIdApiView.as_view()),
]
