from rest_framework.test import APITestCase
from ..models import Provider, ServiceArea

from . import testing_data


class TestSetUp(APITestCase):

    def setUp(self):

        self.point_present_in_polygon = testing_data.point_1
        self.point_present_no_polygon = testing_data.point_2

        self.polygon_1 = testing_data.polygon_1
        self.polygon_2 = testing_data.polygon_2

        self.test_provider_1 = Provider.objects.create(name="Test1",
                                                       email="test@gmail.com",
                                                       phone_number="+164652611",
                                                       language="English",
                                                       currency="USD")

        self.test_provider_2 = Provider.objects.create(name="Test2",
                                                       email="test2@gmail.com",
                                                       phone_number="+1645892611",
                                                       language="Spanish",
                                                       currency="GBP")

        self.service_area_1 = ServiceArea.objects.create(name="TestServiceArea1",
                                                         price="58.54",
                                                         location=self.polygon_1,
                                                         provider=self.test_provider_1)

        self.service_area_2 = ServiceArea.objects.create(name="TestServiceArea1",
                                                         price="58.54",
                                                         location=self.polygon_2,
                                                         provider=self.test_provider_2)

        self.provider_create_payload = {
            "id": 1,
            "name": "Test1",
            "email": "test@gmail.com",
            "phone_number": "+164652611",
            "language": "English",
            "currency": "USD"
        }

        self.provider_update_payload = {

            "name": "Test1 - Updated",
            "email": "test@gmail.com",
            "phone_number": "+164652611",
            "language": "English",
            "currency": "USD"

        }

        self.service_area_update_payload = {
            "provider_name": "David Boon - Updated",
            "name": "New York City",
            "price": "78.54",
            "location": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            40.828095522590786,
                            -74.4374796112359
                        ],
                        [
                            40.87009757372352,
                            -73.90834633253051
                        ],
                        [
                            40.57924559768349,
                            -73.84792061860428
                        ],
                        [
                            40.65362649632197,
                            -74.46687590449731
                        ],
                        [
                            40.828095522590786,
                            -74.4374796112359
                        ]
                    ]
                ]
            },
            "provider": self.test_provider_1.pk
        }

        super().setUp()
