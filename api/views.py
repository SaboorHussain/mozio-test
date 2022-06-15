from rest_framework import views, generics
from django.shortcuts import get_object_or_404
from django.contrib.gis.geos import Point
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProviderSerializer, ServiceAreaSerializer
from .models import Provider, ServiceArea


from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.


class providerCreate(generics.GenericAPIView):
    serializer_class = ProviderSerializer

    def post(self, request):
        serializer = ProviderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class providerList(generics.ListAPIView):
    serializer_class = ProviderSerializer

    def get(self, request):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)

        return Response(serializer.data)


class providerUpdate(generics.GenericAPIView):
    serializer_class = ProviderSerializer

    def put(self, request, pk):
        provider = get_object_or_404(Provider, pk=pk)

        serializer = ProviderSerializer(instance=provider, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class providerDelete(views.APIView):
    def delete(self, request, pk):

        provider = get_object_or_404(Provider, pk=pk)
        provider.delete()

        return Response({"response": "Item is deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class serviceAreaCreate(generics.GenericAPIView):
    serializer_class = ServiceAreaSerializer

    def post(self, request):
        serializer = ServiceAreaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class serviceAreaList(generics.ListAPIView):
    serializer_class = ServiceAreaSerializer

    def get(self, request):
        service_areas = ServiceArea.objects.all()
        serializer = ServiceAreaSerializer(service_areas, many=True)

        return Response(serializer.data)


class serviceAreaUpdate(generics.GenericAPIView):
    serializer_class = ServiceAreaSerializer

    def put(self, request, pk):
        service_area = get_object_or_404(ServiceArea, pk=pk)

        serializer = ServiceAreaSerializer(
            instance=service_area, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class serviceAreaDelete(views.APIView):
    def delete(self, request, pk):

        service_area = get_object_or_404(ServiceArea, pk=pk)
        service_area.delete()

        return Response({"response": "Item is deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class polygonListByLatLong(generics.ListAPIView):

    serializer_class = ServiceAreaSerializer

    lat_param_config_swagger = openapi.Parameter(
        "lat", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)

    long_param_config_swagger = openapi.Parameter(
        "long", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[lat_param_config_swagger, long_param_config_swagger])
    def get(self, request):
        lat = request.GET.get('lat')
        long = request.GET.get('long')

        if lat is not None and long is not None:

            point = Point(float(lat), float(long))
            service_areas = ServiceArea.objects.filter(
                location__contains=point)

            serializer = ServiceAreaSerializer(service_areas, many=True)

            return Response(serializer.data)
        else:
            return Response({"response": "Please provide valid coordinates."})
