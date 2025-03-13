from django.db import models
import uuid

class Brand(models.Model):
    """Модель для представления бренда автомобиля."""
    title = models.CharField(max_length=255, verbose_name='Название бренда')  # Название бренда
    img = models.ImageField(upload_to='brands/', max_length=255, verbose_name='Логотип')  # Логотип или изображение бренда

    def __str__(self):
        return self.title  # Возвращает название бренда при выводе объекта

class CarModel(models.Model):
    """Модель для представления модели автомобиля, связанной с брендом."""
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд')  # Связь с моделью Brand
    title = models.CharField(max_length=255, verbose_name='Название модели')  # Название модели автомобиля
    model_3d = models.FileField(upload_to='3d_models/', null=True, blank=True, verbose_name='3D модель')  # 3D модель автомобиля

    def __str__(self):  
        return self.title  # Возвращает название модели при выводе объекта


class Spoiler(models.Model):
    """Модель для представления спойлера автомобиля."""
    title = models.CharField(max_length=255, verbose_name='Название спойлера')  # Название спойлера
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')  # Связь с моделью CarModel
    model_3d = models.FileField(upload_to='3d_models/', null=True, blank=True, verbose_name='3D модель спойлера')  # 3D модель спойлера


class Color(models.Model):
    """Модель для представления цвета автомобиля."""
    title = models.CharField(max_length=255, verbose_name='Название цвета')  # Название цвета
    img = models.ImageField(upload_to='colors/', verbose_name='Изображение цвета')  # Изображение цвета

    def __str__(self):
        return self.title  # Возвращает название цвета при выводе объекта


class Discs(models.Model):
    """Модель для представления дисков автомобиля."""
    title = models.CharField(max_length=255, verbose_name='Название диска')  # Название диска
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')  # Связь с моделью CarModel
    model_3d = models.FileField(upload_to='3d_models/', null=True, blank=True, verbose_name='3D модель диска')  # 3D модель диска

    def __str__(self):
        return self.title  # Возвращает название диска при выводе объекта


class Tinting(models.Model):
    """Модель для представления тонировки автомобиля."""
    title = models.CharField(max_length=255, verbose_name='Название тонировки')  # Название тонировки
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')  # Связь с моделью CarModel
    model_3d = models.FileField(upload_to='3d_models/', null=True, blank=True, verbose_name='3D модель тонировки')  # 3D модель тонировки

    def __str__(self):
        return self.title  # Возвращает название тонировки при выводе объекта


class Restyling(models.Model):
    """Модель для представления рестайлинга автомобиля."""
    title = models.CharField(max_length=255, verbose_name='Название рестайлинга')  # Название рестайлинга
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')  # Связь с моделью CarModel
    model_3d = models.FileField(upload_to='3d_models/', null=True, blank=True, verbose_name='3D модель рестайлинга')  # 3D модель рестайлинга


class Bumper(models.Model):
    """Модель для представления переднего бампера автомобиля."""
    title = models.CharField(max_length=255, verbose_name='Название бампера')  # Название бампера
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')  # Связь с моделью CarModel
    model_3d = models.FileField(upload_to='3d_models/', null=True, blank=True, verbose_name='3D модель бампера')  # 3D модель бампера

    def __str__(self):
        return self.title  # Возвращает название бампера при выводе объекта


class RearBumper(models.Model):
    """Модель для представления заднего бампера автомобиля."""
    title = models.CharField(max_length=255, verbose_name='Название заднего бампера')  # Название заднего бампера
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')  # Связь с моделью CarModel
    model_3d = models.FileField(upload_to='3d_models/', null=True, blank=True, verbose_name='3D модель заднего бампера')  # 3D модель заднего бампера

    def __str__(self):
        return self.title  # Возвращает название заднего бампера при выводе объекта


class SideSkirt(models.Model):
    """Модель для представления порога автомобиля."""
    title = models.CharField(max_length=255, verbose_name='Название порога')  # Название порога
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель')  # Связь с моделью CarModel
    model_3d = models.FileField(upload_to='3d_models/', null=True, blank=True, verbose_name='3D модель порога')  # 3D модель порога

    def __str__(self):
        return self.title  # Возвращает название порога при выводе объекта


# В конец файла models.py добавьте:
class Car(models.Model):
    """Модель для представления настроенного автомобиля."""
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Уникальный идентификатор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, verbose_name='Модель автомобиля')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Цвет')
    
    # Опциональные компоненты тюнинга
    spoiler = models.ForeignKey(Spoiler, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Спойлер')
    discs = models.ForeignKey(Discs, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Диски')
    tinting = models.ForeignKey(Tinting, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тонировка')
    restyling = models.ForeignKey(Restyling, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Рестайлинг')
    bumper = models.ForeignKey(Bumper, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Передний бампер')
    rear_bumper = models.ForeignKey(RearBumper, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Задний бампер')
    side_skirt = models.ForeignKey(SideSkirt, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пороги')
    
    title = models.CharField(max_length=255, blank=True, verbose_name='Название конфигурации')
    
    def __str__(self):
        return f"{self.car_model} - {self.title or self.uuid}"