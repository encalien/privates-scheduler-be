from rest_framework import generics

from scheduler.models import Customer, TimeSlot
from scheduler.serializers.timeslot_serializer import TimeslotSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the scheduler index.")

class TimeslotListCreateView(generics.ListCreateAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeslotSerializer

class TimeslotRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeslotSerializer

@api_view(['POST'])
def book_timeslot(request, pk):
    body = request.data

    try:
        timeslot = TimeSlot.objects.get(pk=pk)
        if timeslot.customer:
            return Response(
                status=400, 
                data=f"This slot is already taken by a customer {timeslot.customer}"
            )
    except TimeSlot.DoesNotExist:
        return Response(status=404)

    try:
        customer = Customer.objects.get(email=body["email"])
    except Customer.DoesNotExist:
        customer = Customer.objects.create(
            first_name=body["first_name"],
            last_name=body["last_name"],
            email=body["email"]
        )
        
    try:
        timeslot.book(customer)
    except:
        return Response(status=400, data="Unexpected error occured. Timeslot was not booked.")
    
    
    serializer = TimeslotSerializer(timeslot)
    return Response(serializer.data)
    