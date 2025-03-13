"""
Simulating rolling a die until the cumulative sum of 100 is reached
"""
import random
def simulate_rolls():
    total = 0
    ones_count = 0
    sixes_count = 0
    while total < 100:
        roll = random.randint(1, 6)
        total += roll
        if roll == 1:
            ones_count += 1
        elif roll == 6:
            sixes_count += 1
    return ones_count, sixes_count

# Repeating the simulation 1000 times 
num_simulations = 1000
ones_total = 0
sixes_total = 0

for _ in range(num_simulations):
    ones_count, sixes_count = simulate_rolls()
    ones_total += ones_count
    sixes_total += sixes_count
print(f"Total 1's: {ones_total}")
print(f"Total 6's: {sixes_total}")

"""
My hypothesis is that 1 appears more frequently than 6 overall because 1 appears more often in the early stages of the game, before larger rolls like 
6 have the chance to accumulate. The faster-moving 6 rolls likely end the game sooner, but 1's smaller increments show up more often.
"""
