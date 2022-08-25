# from django.conf.urls import url
from django.urls import path, include
from .views import MataKuliahApiView, MataKuliahIdApiView

urlpatterns = [
    path('matakuliah', MataKuliahApiView.as_view()),
    path('matakuliah/<int:matkul_id>', MataKuliahIdApiView.as_view()),
]
