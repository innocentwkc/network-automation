# Documenation for Simple Cisco Automation Scripts (SCAS)

These are the docs, to edit README later

## Data

### Config files

### Logs

## Modules

### ip_generator.py

```python
# Import the generate_ip_list function from the ip_generator module.
from ip_generator import generate_ip_list

# Define the subnet and the starting IP address.
subnet = '172.18.209.0/25'
start_address = '172.18.209.2'  # Exclude the first IP, typically reserved for a core switch or router.

# Generate the list of IP addresses starting from the specified address in the subnet.
ip_list = generate_ip_list(subnet, start_address)

# Print the list of generated IP addresses return array of IP address.
print(ip_list)

```