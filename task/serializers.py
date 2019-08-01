from rest_framework import serializers
from .models import GuardianRestAPI


class GuardianRestAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = GuardianRestAPI
        fields = ("sectionName", "webTitle")