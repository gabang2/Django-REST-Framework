from rest_framework.response import Response
from rest_framework.views import APIView

from student.models import Student, Class
from student.serializers import StudentSerializer, ClassSerializer


class StudentList(APIView):
    def get(self, request):
        model = Student.objects.all()
        serializer = StudentSerializer(model, many=True)
        return Response(serializer.data)


class ClassList(APIView):
    def get(self, request):
        model = Class.objects.all()
        serializer = ClassSerializer(model, many=True)
        return Response(serializer.data)
