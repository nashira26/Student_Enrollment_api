from rest_framework import serializers
from .models import FunnelStatus, Student, Log

class FunnelStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunnelStatus
        fields = ['id', 'name']

class StudentSerializer(serializers.ModelSerializer):
    # restrict choices for status field
    status = serializers.SlugRelatedField(
        queryset=FunnelStatus.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Student
        fields = ['id', 'name', 'status']

    # override custom update method
    def update(self, instance, validated_data):
        status = validated_data.get('status', instance.status)
        instance.status = status
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
class LogSerializer(serializers.ModelSerializer):
    student_name = StudentSerializer()
    status_before = FunnelStatusSerializer()
    status_after = FunnelStatusSerializer()
    class Meta:
        model = Log
        fields = ['id', 'student_name', 'status_before', 'status_after', 'timestamp']