from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from utils.helper import writeResponse
from .serializers import MataKuliahSerializer
from .models import MataKuliah

# Create your views here.


class MataKuliahApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        matakuliah = MataKuliah.objects.filter()
        serializer = MataKuliahSerializer(matakuliah, many=True)

        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = {
            'matkul_name': request.data.get('matkul_name'),
            'nama_dosen': request.data.get('nama_dosen'),
            'jumlah_sks': request.data.get('jumlah_sks'),
            'ruangan': request.data.get('ruangan'),
            'deskripsi': request.data.get('deskripsi'),
            'semester': request.data.get('semester'),
        }

        serializer = MataKuliahSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_201_CREATED, message='OK', data=serializer.data)


class MataKuliahIdApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, matkul_id):
        try:
            return MataKuliah.objects.get(matkul_id=matkul_id)
        except MataKuliah.DoesNotExist:
            return None

    def get(self, request, matkul_id, *args, **kwargs):
        matkul_instance = self.get_object(matkul_id)
        if not matkul_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        serializer = MataKuliahSerializer(matkul_instance)
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def put(self, request, matkul_id, *args, **kwargs):
        matkul_instance = self.get_object(matkul_id)
        if not matkul_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        serializer = MataKuliahSerializer(
            instance=matkul_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def delete(self, request, matkul_id, *args, **kwargs):
        matkul_instance = self.get_object(matkul_id)
        if not matkul_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        matkul_instance.delete()

        return writeResponse(status_code=status.HTTP_200_OK, message="OK")
