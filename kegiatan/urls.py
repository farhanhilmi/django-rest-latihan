from django.urls import path, include
from .views import KegiatanApiView, KegiatanIdApiView, AttendanceApiView

urlpatterns = [
    path('kegiatan', KegiatanApiView.as_view()),
    path('kegiatan/<int:id_kegiatan>', KegiatanIdApiView.as_view()),
    path('kegiatan/<int:id_kegiatan>/attendance/add',
         AttendanceApiView.as_view()),
    # path('matakuliah/<int:matkul_id>', MataKuliahIdApiView.as_view()),
]
