import sys
import os
import unittest
from unittest.mock import patch

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src"))
)
from src.ip_geolocation.ip_geolocation import IPAddress, Coordinates


class TestIPAddress(unittest.TestCase):
    @patch("src.ip_geolocation.ip_geolocation.requests.get")
    def test_get_coordinates_success(self, mock_get):
        # Mock API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "status": "success",
            "lat": 37.751,
            "lon": -97.822,
        }

        ip = IPAddress("8.8.8.8")
        coordinates = ip.get_coordinates()
        self.assertEqual(coordinates, Coordinates(37.751, -97.822))

    @patch("src.ip_geolocation.ip_geolocation.requests.get")
    def test_get_coordinates_failure(self, mock_get):
        # Mock API failure response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "status": "fail",
            "message": "invalid query",
        }

        ip = IPAddress("999.999.999.999")
        coordinates = ip.get_coordinates()
        self.assertIsNone(coordinates)

    @patch("src.ip_geolocation.ip_geolocation.requests.get")
    def test_api_error_handling(self, mock_get):
        # Mock an exception during the API call
        mock_get.side_effect = Exception("API unreachable")

        ip = IPAddress("1.1.1.1")
        coordinates = ip.get_coordinates()
        self.assertIsNone(coordinates)

    def test_ip_geolocation_repr(self):
        ip = IPAddress("192.168.1.1")
        self.assertEqual(repr(ip), "IPAddress('192.168.1.1')")


class TestCoordinates(unittest.TestCase):
    def test_coordinates_equality(self):
        c1 = Coordinates(37.751, -97.822)
        c2 = Coordinates(37.751, -97.822)
        c3 = Coordinates(40.7128, -74.006)
        self.assertEqual(c1, c2)
        self.assertNotEqual(c1, c3)

    def test_coordinates_repr(self):
        c = Coordinates(37.751, -97.822)
        self.assertEqual(repr(c), "Coordinates(37.751, -97.822)")


if __name__ == "__main__":
    unittest.main()
