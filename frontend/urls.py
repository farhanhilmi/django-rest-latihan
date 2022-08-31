from django.urls import path, include
from .views import accordion, user, index

urlpatterns = [
    # home
    path('', index.home, name='home'),

    path('accordion', accordion.accordion, name='accordion'),
    path('accordion/add', accordion.add),
    path('accordion/update/<int:id>', accordion.update),
    path('accordion/delete/<int:id>', accordion.delete),

    # User
    path('login', user.login, name='login'),
    path('login/validate_login', user.validate_login, name='validate_login'),

    # path('kegiatan/<int:id_kegiatan>', KegiatanIdApiView.as_view()),
    # path('kegiatan/<int:id_kegiatan>/attendance/add',
    #      AttendanceApiView.as_view()),
    # path('matakuliah/<int:matkul_id>', MataKuliahIdApiView.as_view()),
]
