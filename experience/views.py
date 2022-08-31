from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Experience
from .serializers import ExperienceSerializer
from utils.helper import writeResponse

# Create your views here.


class ExperienceApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        experience = Experience.objects.all()
        serializer = ExperienceSerializer(experience, many=True)

        return writeResponse(status_code=status.HTTP_200_OK, message='OK', data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = {
            'experience_type': request.data.get('experience_type'),
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'start_date': request.data.get('start_date'),
            'end_date': request.data.get('end_date'),
        }

        serializer = ExperienceSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_201_CREATED, message='OK', data=serializer.data)


class ExperienceApiIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, experience_id):
        try:
            return Experience.objects.get(id_experience=experience_id)
        except Experience.DoesNotExist:
            return None

    def get(self, request, experience_id, *args, **kwargs):
        experience_instance = self.get_object(experience_id)
        if not experience_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        serializer = ExperienceSerializer(
            experience_instance, context={"request": request})
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def put(self, request, experience_id, *args, **kwargs):
        experience_instance = self.get_object(experience_id)
        if not experience_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        serializer = ExperienceSerializer(
            instance=experience_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def delete(self, request, experience_id, *args, **kwargs):
        experience_instance = self.get_object(experience_id)
        if not experience_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        experience_instance.delete()
        return writeResponse(status_code=status.HTTP_200_OK, message="OK")
