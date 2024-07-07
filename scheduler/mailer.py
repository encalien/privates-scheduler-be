from scheduler.models import TimeSlot
from django.core.mail import send_mail


def send_confirmation_emails(timeslot: TimeSlot):
    send_mail(
        "Timeslot booked!",
        f"Hello {timeslot.customer.first_name}!\nThis is an automatic email confirming that you booked the following timeslot:\nDate: {timeslot.start_date.strftime('%A, %-d.%-m.%Y %H:%M')} - {timeslot.end_date.strftime('%H:%M')}\nInstructor: {timeslot.provider.first_name} {timeslot.provider.last_name}\nIf you wish to change or cancel your timeslot please contact your instructor directly on {timeslot.provider.email}.\nEnjoy your class!",
        "info@wcs.si",
        [timeslot.customer.email],
    )

    send_mail(
        "Timeslot booked!",
        f"Hello {timeslot.provider.first_name}!\nThis is an automatic email informing you about the following new booking:\nDate: {timeslot.start_date.strftime('%A, %-d.%-m.%Y %H:%M')} - {timeslot.end_date.strftime('%H:%M')}\nCustomer: {timeslot.customer.first_name} {timeslot.customer.last_name}\nIf you wish to change or cancel your timeslot please contact support.",
        "info@wcs.si",
        [timeslot.provider.email],
    )

    send_mail(
        "Timeslot booked!",
        f"Hello {timeslot.owner.first_name}!\nThis is an automatic email informing you about the following new booking:\nDate: {timeslot.start_date.strftime('%A, %-d.%-m.%Y %H:%M')} - {timeslot.end_date.strftime('%H:%M')}\nCustomer: {timeslot.customer.first_name} {timeslot.customer.last_name}\nInstructor: {timeslot.provider.first_name} {timeslot.provider.last_name}",
        "info@wcs.si",
        [timeslot.owner.email],
    )
