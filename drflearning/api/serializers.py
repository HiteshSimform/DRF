from rest_framework import serializers

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 100)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)

from .models import StudentModel

class StudentSerializer(serializers.Serializer):
    class Meta:
        model = StudentModel
        fields = '__all__'