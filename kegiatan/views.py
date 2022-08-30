from rest_framework import status
from rest_framework.views import APIView

from utils.helper import writeResponse
from .serializers import AttendanceSerializer, KegiatanSerializer
from .models import Kegiatan, Attendance
# Create your views here.


class KegiatanApiView(APIView):
    def get(self, request, *args, **kwargs):
        kegiatan = Kegiatan.objects.all()
        serializer = KegiatanSerializer(kegiatan, many=True)

        return writeResponse(status_code=status.HTTP_200_OK, message='OK', data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = {
            'nama_kegiatan': request.data.get('nama_kegiatan'),
            'waktu_kegiatan': request.data.get('waktu_kegiatan'),
            'deskripsi': request.data.get('deskripsi'),
        }

        serializer = KegiatanSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_201_CREATED, message='OK', data=serializer.data)


class KegiatanIdApiView(APIView):
    def get_object(self, id_kegiatan):
        try:
            return Kegiatan.objects.get(id_kegiatan=id_kegiatan)
        except Kegiatan.DoesNotExist:
            return None

    def get(self, request, id_kegiatan, *args, **kwargs):
        kegiatan_instance = self.get_object(id_kegiatan)
        if not kegiatan_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        serializer = KegiatanSerializer(kegiatan_instance)
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def put(self, request, id_kegiatan, *args, **kwargs):
        kegiatan_instance = self.get_object(id_kegiatan)
        if not kegiatan_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        serializer = KegiatanSerializer(
            instance=kegiatan_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def delete(self, request, id_kegiatan, *args, **kwargs):
        kegiatan_instance = self.get_object(id_kegiatan)
        if not kegiatan_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        kegiatan_instance.delete()

        return writeResponse(status_code=status.HTTP_200_OK, message="OK")


class AttendanceApiView(APIView):
    def get_object_kegiatan(self, id_kegiatan):
        try:
            return Kegiatan.objects.get(id_kegiatan=id_kegiatan)
        except Kegiatan.DoesNotExist:
            return None

    def post(self, request, id_kegiatan, *args, **kwargs):
        kegiatan_instance = self.get_object_kegiatan(id_kegiatan)
        if not kegiatan_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        data = {
            'nama_peserta': request.data.get('nama_peserta'),
            'domisili_peserta': request.data.get('domisili_peserta'),
        }

        serializer = AttendanceSerializer(
            data=data, context={'kegiatan_instance': kegiatan_instance})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_201_CREATED, message='OK', data=serializer.data)
