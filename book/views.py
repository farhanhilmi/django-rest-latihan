from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from utils.helper import deleteFile, writeResponse
from .serializers import BookSerializer
from .models import Book


class BookApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        books = Book.objects.filter()

        serializer = BookSerializer(
            books, many=True)
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = {
            'id_book_reference': request.data.get('id_book_reference'),
            'title': request.data.get('title'),
            'author': request.data.get('author'),
            'description': request.data.get('description'),
            'image': request.data['image'],
        }

        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_201_CREATED, message="OK", data=serializer.data)

        # return writeResponse(code=status.HTTP_400_BAD_REQUEST, status="BAD REQUEST", data=serializer.errors)


class BookApiIdView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, book_id):
        try:
            return Book.objects.get(id_book=book_id)
        except Book.DoesNotExist:
            return None

    def get(self, request, book_id, *args, **kwargs):
        book_instance = self.get_object(book_id)
        if not book_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        serializer = BookSerializer(
            book_instance)
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def put(self, request, book_id, *args, **kwargs):
        book_instance = self.get_object(book_id)
        if not book_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        serializer = BookSerializer(
            instance=book_instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def delete(self, request, book_id, *args, **kwargs):
        book_instance = self.get_object(book_id)
        if not book_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        book_instance.delete()
        return writeResponse(status_code=status.HTTP_200_OK, message="OK")
