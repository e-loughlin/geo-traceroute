import unittest
from src.map.map import WorldMap


class TestWorldMap(unittest.TestCase):
    def test_add_locations_and_draw(self):
        # Create a WorldMap instance
        world_map = WorldMap()

        # Add a set of locations
        locations = [
            (51.5074, -0.1278),  # London
            (48.8566, 2.3522),  # Paris
            (40.7128, -74.0060),  # New York
            (34.0522, -118.2437),  # Los Angeles
        ]
        world_map.add_locations(locations)

        # Verify locations are added
        self.assertEqual(world_map.locations, locations)

        # Test the draw method (this will visually display the map)
        # Note: This test doesn't assert anything; it's for manual visual inspection.
        world_map.draw()


if __name__ == "__main__":
    unittest.main()
