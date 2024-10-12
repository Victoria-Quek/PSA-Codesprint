import pandas as pd
import numpy as np
import random
import string
# from datetime import datetime, timedelta

from ShipYard import *

# 1. Generate Port Data
total_ports = np.random.randint(10, 30)
print("\nNumber of ports:", total_ports)

def generate_ports(num_ports):
    ports_data = []
    
    def generate_random_port_code():
        return 'P' + ''.join(random.choices(string.digits, k = 3))
    
    for i in range(num_ports):
        ports_data.append({
            'port_code': generate_random_port_code()
        })
    return pd.DataFrame(ports_data)

port_data = generate_ports(total_ports)

print("Port Data:")
print(port_data.head(10))


# 2. Generate Ship Data
total_ships = np.random.randint(10**3, 5*10**3)
print("\nNumber of ships:", total_ships)

def generate_ships(num_ships):
    ships_data = []
    
    def generate_random_ship_code():
        return 'S' + ''.join(random.choices(string.digits, k = 7))
    
    for i in range(num_ships):
        ship_id = generate_random_ship_code()
        base_length = np.random.randint(1, 10) # how many containers can be held at the base length
        base_breadth = np.random.randint(1, 5) # how many containers can be held at the base breadth
        base_area = base_length * base_breadth # how many containers can be held at the base itself
        container_matrix = [[0] * base_breadth for j in range(base_length)]
        print(container_matrix)
        containers_per_stack = np.random.randint(1, 4) # max number of containers stacked is 4
        max_capacity = base_area * containers_per_stack
        two_random_ports = port_data.sample(n=2) # generate an arbitrary origin and destination port      
        origin_port = two_random_ports.iloc[0]['port_code'] # origin port
        destination_port = two_random_ports.iloc[1]['port_code'] # destination port
        print(origin_port)
        print(destination_port)
        # loading_time = Ship.getLoadingTime()
        # current_time = datetime.now()
        # arrival_time = (current_time + timedelta(hours=random.randint(1, 100))).strftime('%Y-%m-%d %H:%M:%S')
        # departure_time = (arrival_time + timedelta(hours=random.randint(2, 130))).strftime('%Y-%m-%d %H:%M:%S')
        
        ships_data.append({
            'ship_id': ship_id,
            'base_area': base_area,
            'containers_per_stack': containers_per_stack,
            'max_capacity': max_capacity,
            'origin_port': origin_port,
            # 'loading_time': loading_time,
            # 'arrival_time': arrival_time,
            # 'departure_time': departure_time
        })
    return pd.DataFrame(ships_data)

ships_data = generate_ships(total_ships)

print("Ships Data:")
print(ships_data.head(50))


# 3. Generate Container data
total_containers = np.random.randint(5*10**5, 10**6)
print("\nNumber of containers:", total_containers)

def generate_containers(num_containers):
    containers_data = []
    
    def generate_random_container_code():
        return 'C' + ''.join(random.choices(string.digits, k = 10))
    
    container_id = generate_random_container_code(),
    weight = np.random.randint(1000, 20000), # Random weight between 1000 and 20000 kg
    ship_id = random.choice(ships_data['ship_id'].values)  # Randomly assign a container to a ship
    
    for i in range(num_containers):
        containers_data.append({
            'container_id': container_id,
            'weight': weight,
            'ship_id': ship_id,
            
        })
    return pd.DataFrame(containers_data)

containers_data = generate_containers(total_containers)

print("Container Data:")
print(containers_data.head(50))

