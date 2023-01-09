from django.contrib import admin
from listings.models import Band
from listings.models import Listing


class BandAdmin(admin.ModelAdmin):
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ("name", "year_formed", "genre")


class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "band", "sold")


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
