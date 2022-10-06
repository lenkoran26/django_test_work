from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Resume
        fields = '__all__'

