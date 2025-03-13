from django.contrib import admin
from .models import Brand, Spoiler, Color, Tinting, Restyling, CarModel, Discs, Bumper, RearBumper, SideSkirt
        


admin.site.register(Brand)
admin.site.register(Spoiler)
admin.site.register(Color)
admin.site.register(Tinting)
admin.site.register(Restyling)
admin.site.register(CarModel)
admin.site.register(Discs)  # Регистрация с кастомным админом
admin.site.register(Bumper)
admin.site.register(RearBumper)
admin.site.register(SideSkirt)