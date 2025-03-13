from rest_framework import serializers
from .models import Brand, Car, CarModel, Color, Spoiler, Discs, Tinting, Restyling, Bumper, RearBumper, SideSkirt

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title', 'img'] 

class CarModelSerializer(serializers.ModelSerializer):
    brand_name = serializers.ReadOnlyField(source='brand.title')
    
    class Meta:
        model = CarModel
        fields = ['id', 'title', 'brand_name', 'model_3d']

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'model_3d']

class SpoilerSerializer(ComponentSerializer):
    class Meta(ComponentSerializer.Meta):
        model = Spoiler

class DiscsSerializer(ComponentSerializer):
    class Meta(ComponentSerializer.Meta):
        model = Discs

class TintingSerializer(ComponentSerializer):
    class Meta(ComponentSerializer.Meta):
        model = Tinting

class RestylingSerializer(ComponentSerializer):
    class Meta(ComponentSerializer.Meta):
        model = Restyling

class BumperSerializer(ComponentSerializer):
    class Meta(ComponentSerializer.Meta):
        model = Bumper

class RearBumperSerializer(ComponentSerializer):
    class Meta(ComponentSerializer.Meta):
        model = RearBumper

class SideSkirtSerializer(ComponentSerializer):
    class Meta(ComponentSerializer.Meta):
        model = SideSkirt

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'title', 'img']

class CarSerializer(serializers.ModelSerializer):
    car_model = CarModelSerializer()
    color = ColorSerializer()
    spoiler = SpoilerSerializer()
    discs = DiscsSerializer()
    tinting = TintingSerializer()
    restyling = RestylingSerializer()
    bumper = BumperSerializer()
    rear_bumper = RearBumperSerializer()
    side_skirt = SideSkirtSerializer()
    
    class Meta:
        model = Car
        fields = [
            'uuid', 'title', 'created_at',
            'car_model', 'color', 'spoiler', 'discs', 'tinting',
            'restyling', 'bumper', 'rear_bumper', 'side_skirt'
        ]