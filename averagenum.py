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

def calculate_probabilities(num_simulations):
    final_numbers_count = {}
    total_simulations = num_simulations

    for _ in range(num_simulations):
        final_number = simulate_game()
        final_numbers_count[final_number] = final_numbers_count.get(final_number, 0) + 1

    probabilities = {k: v / total_simulations for k, v in final_numbers_count.items()}
    return probabilities

# Set the number of simulations
num_simulations = 1000

probabilities = calculate_probabilities(num_simulations)

for number, probability in sorted(probabilities.items()):
    print(f"Number: {number}, Overall Probability: {probability:.4f}")

sorted_probabilities = sorted(probabilities.items())
cumulative_probabilities = [sum(p[1] for p in sorted_probabilities[:i+1]) for i in range(len(sorted_probabilities))]

plt.plot([p[0] for p in sorted_probabilities], cumulative_probabilities, marker='o')
plt.xlabel('Final Numbers')
plt.ylabel('Cumulative Probability')
plt.title(f'Cumulative Probability Distribution of Final Numbers ({num_simulations} Simulations)')
plt.show()
