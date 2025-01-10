# Geo Trace Route and Map Visualization

This project provides a tool to visualize the geographical locations of the IP addresses obtained from a trace route of a given domain or IP address. The program performs the following steps:

1. It takes an IP address or URL as input.
2. It performs a trace route to get a list of intermediate IP addresses.
3. It fetches the geographical coordinates (latitude, longitude) for each IP address.
4. It plots these locations on a world map using Cartopy and Matplotlib.

## Requirements

Before using this tool, ensure that you have Python 3.x installed. You will also need to install the required libraries, which can be done using `pip`:

```bash
pip install -r requirements.txt
```

### Required Libraries:

- `requests` – For fetching IP geolocation data via an API.
- `cartopy` – For map projections and visualizations.
- `matplotlib` – For creating and displaying the map.

## Setup

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/geo-traceroute.git
cd geo-traceroute
```

### Example Usage

To use this tool, run the following command in your terminal:

```bash
python geo_ping.py <IP_or_URL>
```

Where `<IP_or_URL>` can be an IP address or a domain URL (e.g., `8.8.8.8` or `google.com`).

Example:

```bash
python geo_ping.py 8.8.8.8
```

The program will perform a trace route to the given IP or URL, get the geolocation for each IP address along the way, and display the results on a world map.

## File Descriptions

- **`geo_ping.py`**: The main script that takes an IP address or URL as input, performs a trace route, fetches geolocation data, and draws the map with the locations.
- **`trace_route.py`**: Contains the `trace_route()` function, which performs a trace route and returns a list of IP addresses.
- **`ip_geolocation.py`**: Defines the `IPAddress` and `Coordinates` classes. `IPAddress` fetches the geolocation of an IP address using a free API (ip-api.com), and `Coordinates` represents geographical coordinates.
- **`map.py`**: Defines an abstract base class `AbstractMap` and the `WorldMap` class that uses Cartopy to plot locations on a world map.

## Error Handling

- The program will skip over any IP addresses for which geolocation data cannot be fetched (e.g., private or reserved IP ranges).
- The trace route and geolocation functions handle exceptions and log errors where necessary.

## Contributing

Feel free to fork this project and make improvements! If you have any bug fixes or new features, please submit a pull request. Contributions are welcome.

### Issues

If you encounter any issues or have questions, please open an issue in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Make sure to replace `yourusername` with your actual GitHub username.
