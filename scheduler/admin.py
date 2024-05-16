from django.contrib import admin

from scheduler.models import Customer, TimeSlot


# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        field.name
        for field in Customer._meta.fields
        if field.name not in ["created_at", "updated_at"]
    ]
    search_fields = ("first_name", "last_name", "email")


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = [
        field.name
        for field in TimeSlot._meta.fields
        if field.name not in ["created_at", "updated_at"]
    ]
    search_fields = (
        "start_date",
        "customer__first_name",
        "customer__last_name",
        "status",
    )
