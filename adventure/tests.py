from django.test import TestCase
import coreapi


# Create your tests here.
class TestCoreApi(TestCase):
    def test_client_can_get_schema(self):
        client = coreapi.Client()
        schema = client.get('http://127.0.0.1:8000/api/')
        print(f"{client=}")
        print(f"{schema=}")
