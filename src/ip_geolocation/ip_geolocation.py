import requests


class IPAddress:
    def __init__(self, ip_address: str):
        """Initialize with an IP address."""
        self.ip_address = ip_address

    def get_coordinates(self):
        """
        Fetch the approximate GPS coordinates (latitude, longitude) for this IP address.
        This uses a free IP geolocation API (ip-api.com).
        """
        try:
            response = requests.get(f"http://ip-api.com/json/{self.ip_address}")
            if response.status_code == 200:
                data = response.json()
                if data["status"] == "success":
                    return Coordinates(data["lat"], data["lon"])
                else:
                    # Skip IPs that are in private or reserved ranges
                    if (
                        "private" in data["message"].lower()
                        or "reserved" in data["message"].lower()
                    ):
                        print(
                            f"Skipping {self.ip_address} due to private/reserved range."
                        )
                    else:
                        raise ValueError(f"API error: {data['message']}")
            else:
                raise ConnectionError(f"Failed to reach API: {response.status_code}")
        except Exception as e:
            print(f"Error fetching coordinates for {self.ip_address}: {e}")
            return None

    def __repr__(self):
        return f"IPAddress('{self.ip_address}')"


class Coordinates:
    def __init__(self, latitude: float, longitude: float):
        """Initialize with latitude and longitude."""
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Coordinates({self.latitude}, {self.longitude})"

    def __eq__(self, other):
        """Check equality of two Coordinates objects."""
        if not isinstance(other, Coordinates):
            return NotImplemented
        # Use a tolerance for comparing floats
        tolerance = 1e-6
        return (
            abs(self.latitude - other.latitude) < tolerance
            and abs(self.longitude - other.longitude) < tolerance
        )
