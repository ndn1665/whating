from rest_framework import serializers
from .models import Info

class InfoSerializers(serializers.ModelSerializer):
    class each:
        model = Info
        fields = ('id', 'peoplenums','jobs','locations','ages')