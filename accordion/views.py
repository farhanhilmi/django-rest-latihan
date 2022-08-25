from rest_framework import status
from rest_framework.views import APIView

from django_rest.utils import writeResponse
from .serializers import AccordionSerializer
from .models import Accordion


class AccordionApiView(APIView):
    # serializer_class = AccordionSerializer

    def get(self, request, *args, **kwargs):
        accordions = Accordion.objects.filter()

        serializer = AccordionSerializer(accordions, many=True)
        return writeResponse(code=status.HTTP_200_OK, status="OK", data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'deskripsi': request.data.get('deskripsi'),
        }

        serializer = AccordionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return writeResponse(code=status.HTTP_201_CREATED, status="OK", data=serializer.data)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)

        return writeResponse(code=status.HTTP_400_BAD_REQUEST, status="BAD REQUEST", data=serializer.errors)


class AccordionIdApiView(APIView):
    def get_object(self, accordion_id):
        try:
            return Accordion.objects.get(id_accordion=accordion_id)
        except Accordion.DoesNotExist:
            return None

    def get(self, request, accordion_id, *args, **kwargs):
        accordion_instance = self.get_object(accordion_id)
        if not accordion_instance:
            return writeResponse(code=status.HTTP_404_NOT_FOUND, status="Object not found")

        serializer = AccordionSerializer(accordion_instance)
        return writeResponse(code=status.HTTP_200_OK, status="OK", data=serializer.data)

    def put(self, request, accordion_id, *args, **kwargs):
        accordion_instance = self.get_object(accordion_id)
        if not accordion_instance:
            return writeResponse(code=status.HTTP_404_NOT_FOUND, status="Object not found")

        data = {
            'title': request.data.get('title'),
            'deskripsi': request.data.get('deskripsi'),
        }

        serializer = AccordionSerializer(
            instance=accordion_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return writeResponse(code=status.HTTP_200_OK, status="OK", data=serializer.data)

        return writeResponse(code=status.HTTP_400_BAD_REQUEST, status="BAD REQUEST", data=serializer.errors)

    def delete(self, request, accordion_id, *args, **kwargs):
        accordion_instance = self.get_object(accordion_id)
        if not accordion_instance:
            return writeResponse(code=status.HTTP_404_NOT_FOUND, status="Object not found")

        accordion_instance.delete()

        return writeResponse(code=status.HTTP_200_OK, status="OK")
