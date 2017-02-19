from api.models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

