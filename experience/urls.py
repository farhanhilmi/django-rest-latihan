from django.urls import path, include


from .views import ExperienceApiIdView, ExperienceApiView

urlpatterns = [
    path('experience', ExperienceApiView.as_view()),
    path('experience/<int:experience_id>', ExperienceApiIdView.as_view()),
]
