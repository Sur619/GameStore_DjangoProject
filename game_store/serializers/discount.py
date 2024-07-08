from rest_framework import serializers

from game_store.models import Discount


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = '__all__'