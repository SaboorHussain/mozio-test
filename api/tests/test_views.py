import json
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from ..models import Provider, ServiceArea
from ..serializers import ProviderSerializer, ServiceAreaSerializer
from .test_setup import TestSetUp
# Create your tests here.


client = APIClient()


class TestReadOperations(TestSetUp):

    def test_get_all_providers(self):
        response = client.get(reverse('list-providers'))
        providers = Provider.objects.all()

        serializer = ProviderSerializer(providers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_service_areas(self):
        response = client.get(reverse('list-service-areas'))
        service_areas = ServiceArea.objects.all()

        serializer = ServiceAreaSerializer(service_areas, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCreateOperations(TestSetUp):

    def test_create_provider(self):
        response = client.post(
            reverse('create-provider'),
            data=json.dumps(self.provider_create_payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_service_area(self):
        self.assertEqual(self.service_area_1.provider, self.test_provider_1)


class TestUpdateOperations(TestSetUp):
    def test_update_provider(self):
        response = client.put(
            reverse('update-provider',
                    kwargs={'pk': self.test_provider_1.id}),
            data=json.dumps(self.provider_update_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_service_area(self):
        response = client.put(
            reverse('update-service-area',
                    kwargs={'pk': self.service_area_1.id}),
            data=json.dumps(self.service_area_update_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestDeleteOperations(TestSetUp):
    def test_delete_provider(self):
        response = client.delete(
            reverse('delete-provider', kwargs={'pk': self.test_provider_2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_service_area(self):
        response = client.delete(
            reverse('delete-service-area', kwargs={'pk': self.service_area_2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestListPolygonsByLatLong(TestSetUp):
    def test_list_polygons_by_latlong_with_some_polygons_returned(self):

        response = client.get(reverse('polygon-list-by-latlong') +
                              '?lat=' + str(self.point_present_in_polygon.x) +
                              "&long=" + str(self.point_present_in_polygon.y))

        service_areas = ServiceArea.objects.filter(
            location__contains=self.point_present_in_polygon)

        serializer = ServiceAreaSerializer(service_areas, many=True)
        self.assertEqual(serializer.data, response.data)

    def test_list_polygons_by_latlong_with_no_polygons_returned(self):

        response = client.get(reverse('polygon-list-by-latlong') +
                              '?lat=' + str(self.point_present_no_polygon.x) +
                              "&long=" + str(self.point_present_no_polygon.y))

        service_areas = ServiceArea.objects.filter(
            location__contains=self.point_present_no_polygon)

        serializer = ServiceAreaSerializer(service_areas, many=True)
        self.assertEqual(serializer.data, response.data)
