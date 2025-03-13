from rest_framework import viewsets 
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Brand, Spoiler, Color, Tinting, Restyling, CarModel, Discs, Bumper, RearBumper, SideSkirt, CarModel
from .serializers import BrandSerializer, SpoilerSerializer, ColorSerializer,  TintingSerializer,  RestylingSerializer, CarModelSerializer, DiscsSerializer, BumperSerializer, RearBumperSerializer, SideSkirtSerializer, CarSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class DiscsViewSet(viewsets.ModelViewSet):
    queryset = Discs.objects.all()
    serializer_class = DiscsSerializer  

class SpoilerViewSet(viewsets.ModelViewSet):
    queryset = Spoiler.objects.all()
    serializer_class = SpoilerSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class TintingViewSet(viewsets.ModelViewSet):
    queryset = Tinting.objects.all()
    serializer_class = TintingSerializer


class RestylingViewSet(viewsets.ModelViewSet):
    queryset = Restyling.objects.all()
    serializer_class = RestylingSerializer

class BumperViewSet(viewsets.ModelViewSet):
    queryset = Bumper.objects.all()
    serializer_class = BumperSerializer

class RearBumperViewSet(viewsets.ModelViewSet):
    queryset = RearBumper.objects.all()
    serializer_class = RearBumperSerializer

class SideSkirtViewSet(viewsets.ModelViewSet):
    queryset = SideSkirt.objects.all()
    serializer_class = SideSkirtSerializer



# Добавьте эти функции в ваш существующий views.py

@api_view(['POST'])
def save_car(request):
    """
    Сохраняет настроенный автомобиль и возвращает уникальный идентификатор
    """
    try:
        data = request.data
        
        # Получаем или создаем объекты моделей
        car_model = get_object_or_404(CarModel, id=data.get('car_model_id'))
        
        # Создаем новый объект Car
        car = Car(car_model=car_model)
        
        # Добавляем опциональные компоненты, если они указаны
        if 'color_id' in data:
            car.color = get_object_or_404(Color, id=data.get('color_id'))
        if 'spoiler_id' in data:
            car.spoiler = get_object_or_404(Spoiler, id=data.get('spoiler_id'))
        if 'discs_id' in data:
            car.discs = get_object_or_404(Discs, id=data.get('discs_id'))
        if 'tinting_id' in data:
            car.tinting = get_object_or_404(Tinting, id=data.get('tinting_id'))
        if 'restyling_id' in data:
            car.restyling = get_object_or_404(Restyling, id=data.get('restyling_id'))
        if 'bumper_id' in data:
            car.bumper = get_object_or_404(Bumper, id=data.get('bumper_id'))
        if 'rear_bumper_id' in data:
            car.rear_bumper = get_object_or_404(RearBumper, id=data.get('rear_bumper_id'))
        if 'side_skirt_id' in data:
            car.side_skirt = get_object_or_404(SideSkirt, id=data.get('side_skirt_id'))
        
        # Добавляем опциональное название, если оно указано
        if 'title' in data:
            car.title = data.get('title')
        
        # Сохраняем автомобиль
        car.save()
        
        # Возвращаем UUID для формирования ссылки
        return Response({
            'uuid': car.uuid,
            'share_url': f"/api/car/{car.uuid}/",
        }, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_car(request, uuid):
    """
    Получает настроенный автомобиль по UUID
    """
    try:
        car = get_object_or_404(Car, uuid=uuid)
        
        # Сериализуем и возвращаем данные
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)