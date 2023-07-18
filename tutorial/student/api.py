from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import Student, Class
from student.serializers import StudentSerializer, ClassSerializer


class StudentList(APIView):
    def get(self, request):
        model = Student.objects.all()
        serializer = StudentSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassList(APIView):
    def get(self, request):
        model = Class.objects.all()
        serializer = ClassSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
