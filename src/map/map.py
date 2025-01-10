from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature


class AbstractMap(ABC):
    @abstractmethod
    def add_locations(self, locations):
        """Add a list of GPS coordinates (latitude, longitude) to the map."""
        pass

    @abstractmethod
    def draw(self):
        """Render the map."""
        pass


class WorldMap(AbstractMap):
    def __init__(self):
        self.locations = []

    def add_locations(self, locations):
        """Add a list of GPS coordinates (latitude, longitude)."""
        self.locations.extend(locations)

    def draw(self):
        """Draw the world map with pins and connecting lines."""
        # Create a figure with a Cartopy GeoAxes
        fig, ax = plt.subplots(subplot_kw={"projection": ccrs.PlateCarree()})
        ax.set_global()
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.BORDERS, linestyle=":")

        # Extract latitudes and longitudes from the Coordinates objects
        lats = [location.latitude for location in self.locations]
        lons = [location.longitude for location in self.locations]

        # Plot each location as a point
        ax.plot(lons, lats, "ro", markersize=5, label="Locations")

        # Draw lines between consecutive locations
        ax.plot(lons, lats, "b-", linewidth=1, label="Connections")

        # Add legend and show the map
        ax.legend()
        plt.show()
