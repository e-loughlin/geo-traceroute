import sys
from src.ip_geolocation.ip_geolocation import IPAddress
from src.map.map import WorldMap
from src.trace_route.trace_route import trace_route


def main():
    if len(sys.argv) != 2:
        print("Usage: python geo_map_ping.py <IP_or_URL>")
        sys.exit(1)

    ip_or_url = sys.argv[1]

    # Step 1: Call trace_route to get a list of IP addresses
    ip_addresses = trace_route(ip_or_url)

    if ip_addresses:
        # Step 2: Get geolocation (coordinates) for each IP address
        locations = []
        for ip in ip_addresses:
            ip_obj = IPAddress(ip)
            location = ip_obj.get_coordinates()
            if location:
                locations.append(location)

        if locations:
            # Step 3: Create a world map and add the locations
            world_map = WorldMap()
            world_map.add_locations(locations)

            # Step 4: Draw the map with the locations
            world_map.draw()
        else:
            print("Unable to get geolocation data for the IP addresses.")
    else:
        print("No IP addresses found from the trace route.")


if __name__ == "__main__":
    main()
