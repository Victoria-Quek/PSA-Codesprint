import pandas as pd
import numpy as np
import random
import string

from ShipYard import *

# Set the parameters
ships = 1000 # Number of ships
foreign_ports = np.random.randint(5, 20) # Number of ports to generate
print("Number of Foreign Ports:", foreign_ports)
ship_types = ['Cargo', 'Container']
ship_sizes = ['Small', 'Medium', 'Large']

np.random.seed(np.random.randint(1, 200)) # set random seed

# Generate synthetic port data
ports = np.random.randint(10, 30)
print("\nNumber of ports:", ports)

def generate_random_port_code():
    return 'P' + ''.join(random.choices(string.digits, k = 3))

port_data = pd.DataFrame({'Port Code': [generate_random_port_code() for _ in range(ports)]})

print("Port Data:")
print(port_data.head(10))

# Generate synthetic container data
def generate_random_container_id():
    return 'C' + ''.join(random.choices(string.digits, k = 10)) + ''.join(random.choices(string.ascii_uppercase, k = 2))

containers = np.random.randint(5*10**4, 10**5)
print("\nNumber of containers:", containers)

container_data = pd.DataFrame({
    'Container ID': [generate_random_container_id() for i in range(containers)], # container ID
    'Weight (kg)': np.random.randint(1000, 20000, size = containers), # Random weight between 1,000 and 20,000 kg
})

print("Container Data:")
print(container_data.head(10))

# Generate synthetic ship data
ships = np.random.randint(10**3, 5*10**3) # Number of ships to generate
print("\nNumber of ships:", ships)

def generate_random_ship_id():
    return 'S' + ''.join(random.choices(string.digits, k = 7)) + ''.join(random.choices(string.ascii_uppercase, k = 1))

ship_data = pd.DataFrame({
    'Ship ID': [generate_random_ship_id() for _ in range(ships)],
    'Maximum Containers': np.random.randint(100, 300, size = ships),
    'Ship Type': np.random.choice(['Cargo', 'Container', 'Tanker'], size = ships),
    'Origin Port': [None] * ships
})

print("Ship Data:")
print(ship_data.head(20))



# Set to track assigned containers
ship_containers = pd.DataFrame()
# {ship_id: [] for ship_id in ship_data['Ship ID']}
assigned_containers_set = set()

# Assign containers to ships
for idx, row in ship_data.iterrows():
    ship_id = row['Ship ID'] # obtain the current ship ID
    available_containers = [container for container in container_data['Container ID'] 
                            if container not in assigned_containers_set] # Filter available containers that have not been assigned yet
    if idx > ships - 5:
        print(idx)
        print(len(available_containers))
    
    num_to_assign = min(row['Maximum Containers'], len(available_containers)) # Do not exceed the maximum capacity of containers
    assigned_containers = random.sample(available_containers, num_to_assign) # Randomly assign available containers to the current ship
        
    ship_containers[ship_id]._append(assigned_containers) # Update the ship's container list and the set of assigned containers
    assigned_containers_set.update(assigned_containers)  # Update containers that have already been assigned to a ship

# Convert the ship_containers dictionary to a DataFrame for easier viewing
# containers_per_ship = pd.DataFrame([
#     {'Ship ID': ship_id, 'Containers': containers}
#     for ship_id, containers in ship_containers.items()
# ])

print("\nContainers per Ship:")
print(ship_containers.head(10))
