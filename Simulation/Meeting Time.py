import numpy as np

T = 60  
W = 15  # Waiting time (minutes)
num_simulations = 100000  

romeo_arrivals = np.random.uniform(0, T, num_simulations)
juliet_arrivals = np.random.uniform(0, T, num_simulations)

# Check if they meet (|X - Y| ≤ W)
successful_meetings = np.abs(romeo_arrivals - juliet_arrivals) <= W

estimated_probability = np.mean(successful_meetings)

print(f"Estimated probability of meeting: {estimated_probability:.4f}")
