from django.contrib import admin
from .models import TripInput, Line, Starting_Stop, Ending_Stop

# Register your models here.
admin.site.register(TripInput)
admin.site.register(Line)
admin.site.register(Starting_Stop)
admin.site.register(Ending_Stop)
