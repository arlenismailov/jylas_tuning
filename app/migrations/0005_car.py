# Generated by Django 5.1.7 on 2025-03-13 09:10

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_wheel_model_remove_wing_model_alter_brand_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Уникальный идентификатор')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Название конфигурации')),
                ('bumper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.bumper', verbose_name='Передний бампер')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carmodel', verbose_name='Модель автомобиля')),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.color', verbose_name='Цвет')),
                ('discs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.discs', verbose_name='Диски')),
                ('rear_bumper', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.rearbumper', verbose_name='Задний бампер')),
                ('restyling', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.restyling', verbose_name='Рестайлинг')),
                ('side_skirt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.sideskirt', verbose_name='Пороги')),
                ('spoiler', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.spoiler', verbose_name='Спойлер')),
                ('tinting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.tinting', verbose_name='Тонировка')),
            ],
        ),
    ]
