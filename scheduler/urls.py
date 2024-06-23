from scheduler.views import TimeslotListCreateView, TimeslotRetrieveUpdateView
from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("timeslots/", TimeslotListCreateView.as_view(), name="timeslot_list"),
    path("timeslots/<int:pk>/", TimeslotRetrieveUpdateView.as_view(), name="timeslot_detail"),
    path("timeslots/<int:pk>/book/", views.book_timeslot, name="book_timeslot"),
]
