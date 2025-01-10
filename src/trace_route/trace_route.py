import subprocess
import re


def trace_route(target: str):
    """
    Perform a traceroute to the target and return a list of IP addresses.
    """
    try:
        # Perform traceroute using the subprocess module
        result = subprocess.run(
            ["traceroute", target], capture_output=True, text=True, check=True
        )

        # Extract the IP addresses using a regular expression
        ip_addresses = re.findall(r"\d+\.\d+\.\d+\.\d+", result.stdout)

        return ip_addresses
    except subprocess.CalledProcessError as e:
        print(f"Error performing traceroute: {e}")
        return []
