from django.contrib import admin

# Register your models here.


from .models import * 



#adjustment of the admin panel
class FlightAdmin(admin.ModelAdmin): #subclass of model admin
    list_display = ("origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flights',)


admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passenger, PassengerAdmin)



