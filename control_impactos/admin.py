from django.contrib import admin
from .models import Supervisor, TeamManager, Empleado, Ausencia, Survey

# Register your models here.

admin.site.register(Supervisor)
admin.site.register(TeamManager)
admin.site.register(Empleado)
admin.site.register(Ausencia)
admin.site.register(Survey)
