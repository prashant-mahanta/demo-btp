from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class MatchSerializer(ModelSerializer):

	class Meta:
		model = Matches
		fields = "__all__"


class MatchDetailsSerializer(ModelSerializer):

	class Meta:
		model = MatchDetails
		fields = "__all__"