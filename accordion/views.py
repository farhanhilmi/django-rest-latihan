from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from utils.helper import writeResponse
from .serializers import AccordionSerializer
from .models import Accordion


class AccordionApiView(APIView):
    permission_classes = [IsAuthenticated]
    # serializer_class = AccordionSerializer

    def get(self, request, *args, **kwargs):
        accordions = Accordion.objects.filter()

        serializer = AccordionSerializer(accordions, many=True)
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'deskripsi': request.data.get('deskripsi'),
        }

        serializer = AccordionSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_201_CREATED, message="OK", data=serializer.data)
        # return Response(serializer.data, message=status.HTTP_201_CREATED)


class AccordionIdApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, accordion_id):
        try:
            return Accordion.objects.get(id_accordion=accordion_id)
        except Accordion.DoesNotExist:
            return None

    def get(self, request, accordion_id, *args, **kwargs):
        accordion_instance = self.get_object(accordion_id)
        if not accordion_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        serializer = AccordionSerializer(accordion_instance)
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def put(self, request, accordion_id, *args, **kwargs):
        accordion_instance = self.get_object(accordion_id)
        if not accordion_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        serializer = AccordionSerializer(
            instance=accordion_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def delete(self, request, accordion_id, *args, **kwargs):
        accordion_instance = self.get_object(accordion_id)
        if not accordion_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        accordion_instance.delete()

        return writeResponse(status_code=status.HTTP_200_OK, message="OK")
