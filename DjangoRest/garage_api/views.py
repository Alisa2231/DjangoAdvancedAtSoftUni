from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from garage_api.models import Manufacturer, Car
from garage_api.serializers import ManufacturerSerializer, CarSerializer


class CarsListApiView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response({'cars': serializer.data})

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CarDetailApiView(APIView):
    def get(self, request, pk):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response({'car': serializer.data})

    def put(self, request, pk):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(instance=car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(instance=car, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        car = Car.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def manufacturers_list_view(request):
    if request.method == 'GET':
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response({'manufacturers': serializer.data})

    if request.method == 'POST':
        serializer = ManufacturerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def manufacturer_details_view(request, pk):
    manufacturer = Manufacturer.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = ManufacturerSerializer(manufacturer)
        return Response({'manufacturer': serializer.data})

    if request.method == 'PUT':
        serializer = ManufacturerSerializer(instance=manufacturer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        serializer = ManufacturerSerializer(instance=manufacturer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        manufacturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)