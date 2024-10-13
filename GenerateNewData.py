import pandas as pd
import numpy as np
import random
import string
from datetime import datetime, timedelta

from ShipYard import *

np.random.seed(2024)

# 1. Generate Port Data
total_ports = 25
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
total_ships = 500
print("\nNumber of ships:", total_ships)

def generate_ships(num_ships):
    ships_data = []
    
    def generate_random_ship_code():
        return 'S' + ''.join(random.choices(string.digits, k = 7))
    
    for i in range(num_ships):
        ship_id = generate_random_ship_code()
        base_length = np.random.randint(2, 10) # how many containers can be held at the base length
        base_breadth = np.random.randint(2, 6) # how many containers can be held at the base breadth
        base_area = int(base_length * base_breadth) # how many containers can be held at the base itself
        max_containers_per_stack = np.random.randint(1, 4) # max number of containers stacked is 4
        max_capacity = int(base_area * max_containers_per_stack)
        empty_slots = int(max_capacity)
        two_random_ports = port_data.sample(n = 2) # generate an arbitrary origin and destination port      
        origin_port = two_random_ports.iloc[0]['port_code'] # origin port
        destination_port = two_random_ports.iloc[1]['port_code'] # destination port
        current_time = datetime.datetime(2024, 10, 13, 18, 00)
        arrival_time = current_time + timedelta(hours = random.randint(1, 100), minutes = random.randint(0, 59), seconds = random.randint(0, 59))
        departure_time = arrival_time + timedelta(hours = random.randint(2, 130), minutes = random.randint(0, 59), seconds = random.randint(0, 59))
        # loading_time = Ship.getLoadingTime()
        
        ships_data.append({
            'ship_id': ship_id,
            'base_length': base_length,
            'base_breadth': base_breadth,
            'base_area': base_area,
            'max_containers_per_stack': max_containers_per_stack,
            'max_capacity': max_capacity,
            'empty_slots': empty_slots,
            'origin_port': origin_port,
            'destination_port': destination_port,
            # 'loading_time': loading_time,
            'arrival_time': arrival_time,
            'departure_time': departure_time
        })
    return pd.DataFrame(ships_data)

ships_data = generate_ships(total_ships)

print("Ships Data:")
print(ships_data.head(50))


# 3. Generate Container data
total_containers = 8000
print("\nNumber of containers:", total_containers)

def generate_containers(ships_data, num_containers):
    containers_data = []
    
    def generate_random_container_code():
        return 'C' + ''.join(random.choices(string.digits, k = 10))
    
    for i in range(num_containers):
        container_id = generate_random_container_code()
        eligible_ships = ships_data.loc[ships_data['empty_slots'] > 0, 'ship_id'].values
        ship_ID = random.choice(eligible_ships)
        ships_data.loc[ships_data['ship_id'] == ship_ID, 'empty_slots'] -= 1
        
        containers_data.append({
            'container_id': container_id,
            'ship_id': ship_ID
            })
    
    return pd.DataFrame(containers_data)

containers_data = generate_containers(ships_data, total_containers)

print("Container Data:")
print(containers_data.head(50))

port_data.to_csv("data/ports.csv", index = False)
ships_data.to_csv("data/ships.csv", index = False)
containers_data.to_csv("data/containers.csv", index = False)
