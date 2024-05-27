from rest_framework import serializers
from home.models import Outlet

class OutletSerializer (serializers.ModelSerializer):
    class Meta :
        model = Outlet
        fields = '__all__'