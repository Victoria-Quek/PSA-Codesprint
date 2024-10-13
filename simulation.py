import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime, timedelta

container_data = pd.read_csv("data/containers.csv")
port_data = pd.read_csv("data/ports.csv")
ship_data = pd.read_csv("data/ships.csv")

# Convert arrival_time and departure_time to datetime objects
ship_data['arrival_time'] = pd.to_datetime(ship_data['arrival_time'])
ship_data['departure_time'] = pd.to_datetime(ship_data['departure_time'])

random.seed(2024)

# Define the simulation time frame
simulation_start = datetime(2024, 10, 13, 0, 0) # Start at 13 Oct 2024 00:00
simulation_end = datetime(2024, 10, 23, 0, 15) # End at 23 Oct 2024 00:15
current_time = simulation_start

# Create flags to track if a ship has been unloaded or loaded
unloaded_ships = set()
loaded_ships = set()

# Number of berths available
num_berths = 5
berths = {i + 1: None for i in range(num_berths)}  # 5 berths initialized as empty

# Function to simulate unloading and loading time
def simulate_container_removal(ship, containers_to_unload):
    # Time taken to remove the containers is based on the stack height
    base_time = 1  # Time per container
    return containers_to_unload * base_time

# Simulate operations for every 10 minutes in the defined time frame
while current_time < simulation_end:
    print(f"\nCurrent Time: {current_time.strftime('%Y-%m-%d %H:%M')}")

    # Display current status of berths
    for berth_id, ship_id in berths.items():
        if ship_id is None:
            print(f"Berth {berth_id}: Empty")
        else:
            print(f"Berth {berth_id}: Ship ID {ship_id}")

    for i in range(1, num_berths + 1):
        # Check if the berth is empty
        if berths[i] is None:
            for index, ship in ship_data.iterrows():
                # Check if the ship is available to be served
                if (ship['arrival_time'] <= current_time < ship['departure_time']) and (ship['ship_id'] not in unloaded_ships):
                    # Simulate unloading containers
                    containers_to_unload = min(ship['max_capacity'] - ship['empty_slots'], 5)  # Example logic
                    if containers_to_unload > 0:
                        time_needed = simulate_container_removal(ship, containers_to_unload)
                        print(f"Serving Ship ID {ship['ship_id']} at Berth {i}: Unloading {containers_to_unload} containers (will take {time_needed} minutes).")
                        # Update time and berth assignment
                        current_time += timedelta(minutes=time_needed)
                        ship['empty_slots'] += containers_to_unload  # Update empty slots
                        unloaded_ships.add(ship['ship_id'])  # Mark as unloaded
                        berths[i] = ship['ship_id']  # Assign ship to berth
                        break

        # Check if any ship at this berth is departing
        if berths[i] is not None:
            ship_id = berths[i]
            ship_row = ship_data[ship_data['ship_id'] == ship_id]

            if not ship_row.empty:
                departure_time = ship_row['departure_time'].values[0]

                # Ensure departure_time is a datetime object for comparison
                if isinstance(departure_time, (pd.Timestamp, str)):
                    if isinstance(departure_time, str):
                        departure_time = pd.to_datetime(departure_time)  # Convert to datetime if it's a string
                    departure_time = departure_time.to_pydatetime()  # Convert pd.Timestamp to datetime

                # Make sure current_time is also a datetime
                if not isinstance(current_time, datetime):
                    raise TypeError("current_time should be a datetime object")

                # Now compare current_time and departure_time
                if current_time >= departure_time:
                    print(f"Ship ID {ship_id} at Berth {i} is departing.")
                    # Simulate loading containers
                    containers_to_load = min(ship_row['empty_slots'].values[0], 3)  # Example logic
                    if containers_to_load > 0:
                        time_needed = simulate_container_removal(ship_row, containers_to_load)
                        print(f"Loading {containers_to_load} containers onto Ship ID {ship_id} (will take {time_needed} minutes).")
                        current_time += timedelta(minutes=time_needed)
                        ship_row['empty_slots'] -= containers_to_load  # Update empty slots
                        loaded_ships.add(ship_id)  # Mark as loaded

                    # Free up the berth
                    berths[i] = None

    # Increment the time by ten minutes
    current_time += timedelta(minutes = 15)
