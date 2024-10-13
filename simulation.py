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

# Simulate operations for every 10 minutes in the defined time frame
while current_time < simulation_end:
    print(f"\nCurrent Time: {current_time.strftime('%Y-%m-%d %H:%M')}")

    # Check for activities in the last 15 minutes for each ship
    for index, ship in ship_data.iterrows():
        
        # Check if the ship has not been unloaded yet
        if (ship['ship_id'] not in unloaded_ships) and (ship['arrival_time'] <= current_time < ship['departure_time']):
            print(f"Ship ID {ship['ship_id']} has arrived.")
            print(f"Capacity: {ship['max_capacity']}")
            # Simulate unloading containers
            containers_to_unload = min(ship['max_capacity'] - ship['empty_slots'], random.randint(1, 15))
            print(f"Unloading {containers_to_unload} containers from Ship ID {ship['ship_id']}.")
            ship['empty_slots'] += containers_to_unload  # Update empty slots
            print(f"Empty Slots on Ship ID {ship['ship_id']}: {ship['empty_slots']}")
            unloaded_ships.add(ship['ship_id'])  # Mark as unloaded

        # Check if the ship is departing and has not been loaded yet
        if (ship['ship_id'] not in loaded_ships) and (ship['departure_time'] <= current_time):
            print(f"Ship ID {ship['ship_id']} is departing.")
            print(f"Capacity: {ship['max_capacity']}")
            # Simulate loading containers
            containers_to_load = min(ship['empty_slots'], random.randint(1, 10))
            print(f"Loading {containers_to_load} containers onto Ship ID {ship['ship_id']}.")
            ship['empty_slots'] -= containers_to_load  # Update empty slots
            print(f"Empty Slots on Ship ID {ship['ship_id']}: {ship['empty_slots']}")
            loaded_ships.add(ship['ship_id'])  # Mark as loaded

    # Increment the time by 15 minutes
    current_time += timedelta(minutes = 15)
