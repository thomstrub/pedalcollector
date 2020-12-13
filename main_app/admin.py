from django.contrib import admin

from .models import Pedal, Session, Board

# Register your models here
admin.site.register(Pedal)
admin.site.register(Session)
admin.site.register(Board)