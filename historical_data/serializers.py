from rest_framework import serializers
from .models import *


class HistoricalDataSerializers(serializers.ModelSerializer):

    class Meta:
        model = HistoriclaData
        fields = '__all__'
