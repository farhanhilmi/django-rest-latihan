from rest_framework import serializers
from .models import Kegiatan, Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

    def create(self, validated_data):
        kegiatan_instance = self.context.get('kegiatan_instance')

        attendance = Attendance.objects.create(**validated_data)
        kegiatan_instance.attendance.add(attendance)
        return attendance


class KegiatanSerializer(serializers.ModelSerializer):
    attendance = AttendanceSerializer(read_only=True, many=True)

    class Meta:
        model = Kegiatan
        fields = ('id_kegiatan', 'nama_kegiatan',
                  'waktu_kegiatan', 'deskripsi', 'attendance')
