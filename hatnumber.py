import random
import matplotlib.pyplot as plt

def simulate_game():
    hat = list(range(1, 2025))

    while len(hat) > 1:
        num1, num2 = random.sample(hat, 2)
        difference = abs(num1 - num2)
        hat.remove(max(num1, num2))
        hat.remove(min(num1, num2))
        hat.append(difference)

    return hat[0]

def run_simulations(num_simulations):
    final_numbers = []

    for _ in range(num_simulations):
        final_number = simulate_game()
        final_numbers.append(final_number)

    return final_numbers

# Set the number of simulations
num_simulations = 1000

# Run simulations and get the list of final numbers
final_numbers_list = run_simulations(num_simulations)

# Plot the results
plt.hist(final_numbers_list, bins=range(0, 2026), align='left', edgecolor='black', alpha=0.7)
plt.xlabel('Final Numbers')
plt.ylabel('Frequency')
plt.title(f'Distribution of Final Numbers (1000 Simulations)')
plt.show()
