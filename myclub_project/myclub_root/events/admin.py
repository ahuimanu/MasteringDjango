from django.contrib import admin

from .models import Event, MyClubUser, Venue

# Register your models here.
# admin.site.register(Venue)
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone")
    ordering = ("name",)
    search_fields = ("name", "address")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (("name", "venue"), "event_date", "description", "manager")
    list_display = ("name", "event_date", "venue")
    list_filter = ("event_date", "venue")
    ordering = "-event_date"


# admin.site.register(Event)
admin.site.register(MyClubUser)
