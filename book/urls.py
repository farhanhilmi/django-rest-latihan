from django.conf import settings
from django.urls import path, include


from .views import BookApiView, BookApiIdView

urlpatterns = [
    path('book', BookApiView.as_view()),
    path('book/<int:book_id>', BookApiIdView.as_view()),
]
