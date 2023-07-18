from rest_framework import serializers

from student.models import Student, Class


class StudentSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)

    class Meta:
        model = Student
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"
