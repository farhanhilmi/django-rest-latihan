# from django.conf.urls import url
from django.urls import path, include
from .views import RegisterApiView, UserTokenPairApiView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('user/register', RegisterApiView.as_view()),

    path('user/login', UserTokenPairApiView.as_view(),
         name='token_obtain_pair'),  # login
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('matakuliah/<int:matkul_id>', MataKuliahIdApiView.as_view()),
]
