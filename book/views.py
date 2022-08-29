from rest_framework import status
from rest_framework.views import APIView

from utils.helper import deleteFile, writeResponse
from .serializers import BookSerializer
from .models import Book


class BookApiView(APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.filter()

        serializer = BookSerializer(
            books, many=True, context={"request": request})
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def post(self, request, *args, **kwargs):
        data = {
            'title': request.data.get('title'),
            'author': request.data.get('author'),
            'description': request.data.get('description'),
            'image': request.data['image'],
        }

        serializer = BookSerializer(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_201_CREATED, message="OK", data=serializer.data)

        # return writeResponse(code=status.HTTP_400_BAD_REQUEST, status="BAD REQUEST", data=serializer.errors)


class BookApiIdView(APIView):
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
            book_instance, context={"request": request})
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def put(self, request, book_id, *args, **kwargs):
        book_instance = self.get_object(book_id)
        if not book_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        serializer = BookSerializer(
            instance=book_instance, data=request.data, partial=True, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return writeResponse(status_code=status.HTTP_200_OK, message="OK", data=serializer.data)

    def delete(self, request, book_id, *args, **kwargs):
        book_instance = self.get_object(book_id)
        if not book_instance:
            return writeResponse(status_code=status.HTTP_404_NOT_FOUND, message="Object not found")

        deleteFile(book_instance.image.path)
        book_instance.delete()
        return writeResponse(status_code=status.HTTP_200_OK, message="OK")
