# Import the ipaddress module to work with IP addresses.
import ipaddress

def generate_ip_list(subnet, start_address):
    """
    Generates a list of IP addresses within a given subnet, starting from a specified address.

    Parameters:
    subnet (str): The subnet in CIDR notation, e.g., '192.168.1.0/24'.
    start_address (str): The starting IP address from which to generate the list, e.g., '192.168.1.2'.
    
    Returns:
    list: A list of string representations of IP addresses from the start_address onwards within the given subnet.
    """
    # Convert the start_address to an IPv4Address object for comparison.
    start_ip = ipaddress.IPv4Address(start_address)

    # Generate the list of IP addresses. This is done by iterating over all IP addresses in the subnet
    # and including those that are greater than or equal to the start_ip.
    return [str(ip) for ip in ipaddress.ip_network(subnet) if ip >= start_ip]
