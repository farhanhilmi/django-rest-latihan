from django.urls import path, include
from .views import accordion, user, index, matkul, kegiatan, book

urlpatterns = [
    # home
    path('', index.home, name='home'),

    # User
    path('login', user.login, name='login'),
    path('logout', user.logout, name='logout'),
    path('login/validate_login', user.validate_login, name='validate_login'),

    # Accordion
    path('accordion', accordion.accordion, name='accordion'),
    path('accordion/add', accordion.add),
    path('accordion/update/<int:id>', accordion.update),
    path('accordion/delete/<int:id>', accordion.delete),

    # Matkul
    path('matkul', matkul.index, name='matkul'),
    path('matkul/add', matkul.add),
    path('matkul/update/<int:id>', matkul.update),
    path('matkul/delete/<int:id>', matkul.delete),

    # Kegiatan
    path('kegiatan', kegiatan.index, name='kegiatan'),
    path('kegiatan/add', kegiatan.add),
    path('kegiatan/update/<int:id>', kegiatan.update),
    path('kegiatan/delete/<int:id>', kegiatan.delete),
    # add attendance
    path('kegiatan/<int:id_kegiatan>/attendance/add', kegiatan.addAttendance),

    # Kegiatan
    path('book', book.index, name='book'),
    path('book/favorite', book.favoriteBook),
    path('book/favorite/add', book.addToFavorite),
    path('book/<int:id>/favorite/delete', book.deleteFromFavorite),



    # path('kegiatan/<int:id_kegiatan>', KegiatanIdApiView.as_view()),
    # path('kegiatan/<int:id_kegiatan>/attendance/add',
    #      AttendanceApiView.as_view()),
    # path('matakuliah/<int:matkul_id>', MataKuliahIdApiView.as_view()),
]
