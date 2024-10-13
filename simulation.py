# Here, we simulate ships in transit unloading specific containers and loading specific containers before departure
# We assume that it takes the same time to remove and add containers, and the containers to be loaded are already available at the port
# We also assume that each ship only transits in Singapore once within the speciifed time frame.

# When a ship arrives and no berth is available, it waits in the queue.
# As time progresses, the simulation checks for berth availability and assigns the next ship in line when a berth becomes free.
# This minimizes delays by ensuring that no berth remains empty if there are ships waiting.

import numpy as np
import random
import pandas as pd
from datetime import datetime, timedelta

# Load data from CSV files
container_data = pd.read_csv("data/containers.csv")
port_data = pd.read_csv("data/ports.csv")
ship_data = pd.read_csv("data/ships.csv")

# Convert arrival_time to datetime object
ship_data['arrival_time'] = pd.to_datetime(ship_data['arrival_time'])

# Simulation settings
num_berths = 5
berths = {i + 1: None for i in range(num_berths)}  # 5 berths initialized as empty
berth_times = {i + 1: None for i in range(num_berths)}  # Track end times for each berth
transaction_log = []  # Log of all transactions
waiting_queue = []  # Queue for waiting ships
simulation_time_step = timedelta(minutes=15)

# Randomly drop off and load containers in Singapore
def random_containers(ship):
    # Random number of containers to drop off and load (within ship's capacity)
    containers_on_board = ship['max_capacity'] - ship['empty_slots']
    containers_to_drop_off = random.randint(1, containers_on_board)
    containers_to_load = random.randint(1, ship['empty_slots'] + containers_to_drop_off)
    
    return containers_to_drop_off, containers_to_load

# Function to calculate total time needed for drop-off and load operations
def calculate_operation_time(containers_to_drop_off, containers_to_load):
    time_per_container = 1  # Assume 1 minute per container
    total_time = (containers_to_drop_off + containers_to_load) * time_per_container
    return total_time

# Assign a ship to a berth if one is available
def assign_berth(ship, current_time):
    for berth_id, end_time in berth_times.items():
        if end_time is None or end_time <= current_time:
            # Calculate drop-off and load operations
            containers_to_drop_off, containers_to_load = random_containers(ship)
            operation_time = calculate_operation_time(containers_to_drop_off, containers_to_load)
            
            # Determine the new departure time based on operation time
            departure_time = current_time + timedelta(minutes=operation_time)
            
            # Log the operation
            transaction_log.append({
                'ship_id': ship['ship_id'],
                'berth': berth_id,
                'arrival_time': current_time,
                'containers_dropped_off': containers_to_drop_off,
                'containers_loaded': containers_to_load,
                'operation_time': operation_time,
                'departure_time': departure_time
            })
            
            # Assign the ship to the berth and update berth timing
            berths[berth_id] = ship['ship_id']
            berth_times[berth_id] = departure_time
            
            print(f"Ship {ship['ship_id']} docked at Berth {berth_id}, "
                  f"dropped off {containers_to_drop_off} containers, loaded {containers_to_load} containers, "
                  f"departing at {departure_time}.")
            
            return True  # Berth assignment successful
    return False  # No berths available

# Process each ship's arrival, docking, and departure
for index, ship in ship_data.iterrows():
    arrival_time = ship['arrival_time']
    
    # Try to assign a berth upon arrival
    if not assign_berth(ship, arrival_time):
        print(f"No berth available for Ship {ship['ship_id']} at {arrival_time}. Adding to the waiting queue.")
        waiting_queue.append((ship, arrival_time))  # Add ship to the queue

# After initial processing, manage the waiting queue and free berths as operations complete
current_time = min(ship_data['arrival_time'])  # Start from the earliest arrival time

while waiting_queue or any(berth_times.values()):
    # Check if any berth is available
    for berth_id, end_time in berth_times.items():
        if end_time and current_time >= end_time:
            print(f"Berth {berth_id} is now free at {current_time}.")
            berths[berth_id] = None  # Free the berth
            berth_times[berth_id] = None  # Reset berth end time
    
    # Try to assign a waiting ship to a free berth
    for ship, arrival_time in waiting_queue[:]:
        if assign_berth(ship, current_time):
            waiting_queue.remove((ship, arrival_time))  # Remove the ship from the queue after assignment
    
    # Move forward in time by the simulation step (15 minutes)
    current_time += simulation_time_step

# After the simulation, print the transaction log
print("\nTransaction Log:")
transaction_log_df = pd.DataFrame(transaction_log)
print(transaction_log_df)
transaction_log_df.to_csv("data/transaction_log.csv", index = False)
