import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

class ShipyardSimulation:
    def __init__(self, num_runs):
        self.num_runs = num_runs
        self.results = []

    def load_container(self, container_type):
        load_time = np.random.exponential(scale=5)  # Example average loading time
        return load_time

    def unload_container(self, container_type):
        unload_time = np.random.exponential(scale=5)  # Example average unloading time
        return unload_time

    def run_single_simulation(self):
        total_time = 0
        containers_to_load = random.randint(5, 20)  # Random number of containers
        for _ in range(containers_to_load):
            load_time = self.load_container("standard")
            total_time += load_time
            unload_time = self.unload_container("standard")
            total_time += unload_time
        return total_time

    def run_simulations(self):
        for _ in range(self.num_runs):
            total_time = self.run_single_simulation()
            self.results.append(total_time)

    def visualize_results(self):
        # Histogram
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 3, 1)
        plt.hist(self.results, bins=30, color='skyblue', edgecolor='black')
        plt.title('Histogram of Total Operation Times')
        plt.xlabel('Total Time')
        plt.ylabel('Frequency')

        # Box Plot
        plt.subplot(1, 3, 2)
        sns.boxplot(data=self.results)
        plt.title('Box Plot of Total Operation Times')
        plt.ylabel('Total Time')

        # CDF
        plt.subplot(1, 3, 3)
        sorted_results = np.sort(self.results)
        yvals = np.arange(1, len(sorted_results) + 1) / len(sorted_results)
        plt.plot(sorted_results, yvals, marker='.', linestyle='none')
        plt.title('Cumulative Distribution Function (CDF)')
        plt.xlabel('Total Time')
        plt.ylabel('Cumulative Probability')

        plt.tight_layout()
        plt.show()

# Example usage
num_simulations = 1000
simulation = ShipyardSimulation(num_runs=num_simulations)
simulation.run_simulations()
simulation.visualize_results()
