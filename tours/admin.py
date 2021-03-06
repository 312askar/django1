from django.contrib import admin

# Register your models here.
from .models import Tour, RegulatTour, TourBooking

@admin.register(TourBooking)
class TourBookingAdmin(admin.ModelAdmin):
    list_display = [
        'regular_tour',
        'place_count',
        'mobile',
        'statuses',
        'is_paid',
        'created',
        'updated'
    ]
    list_filter = [
        'statuses',
        'created',
        'is_paid'
    ]
    list_editable = [
        'statuses',
        'is_paid'
    ]
    search_fields = [
        'mobile',
        'notice',
        'user__first_name'
    ]
    readonly_fields = [
        'mobile',
        'notice',
        'user',
    ]

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created', 'updated', 'is_active', ]
    list_filter = ['created', 'is_active', 'price']
    search_fields = ['title', 'created', 'description']
    list_editable = ['is_active', 'price']


@admin.register(RegulatTour)
class RegulatTourAdmin(admin.ModelAdmin):
    list_display = ['tour', 'start', 'end', 'places_count', 'status']
    list_filter = ['start', 'end', 'status']
    search_fields = ['tour__title', 'start', 'end']
    list_editable = ['status', 'start', 'places_count']
