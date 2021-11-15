from rest_framework import serializers
from .models import Box
from datetime import date, timedelta
from spinny.settings import A1, V1, L1, L2

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['length','breadth','height']
    
    def validate(self, attrs):
        total_area,total_volume= 0, 0
        new_area = attrs['length']*attrs["breadth"]
        new_volume = new_area*attrs["height"]

        objects = Box.objects.all()
        existing_count = objects.count()
        for obj in objects:
            total_area += obj.area
            total_volume += obj.volume

        if (total_area+new_area)/(existing_count+1) > A1:
            raise serializers.ValidationError("Max Area Limit will exceed")
        if (total_volume+new_volume)/(existing_count+1) > V1:
            raise serializers.ValidationError("Max Volume Limit will exceed")
        
        week_count = Box.objects.filter(created_at__gte = date.today()-timedelta(days=7))
        if week_count.count() >= L1:
            raise serializers.ValidationError("Max weekly count Limit will exceed")
        if week_count.filter(creator=self.context['request'].user).count() >= L2:
            raise serializers.ValidationError("Your Max weekly count Limit will exceed")

        return attrs

class ListBoxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['length','breadth','height','area','volume']

class ListBoxesStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['length','breadth','height','area','volume','creator','updated_at']
