from itertools import combinations, product
import random
import matplotlib.pyplot as plt

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return None

def is_valid(expression, remaining_numbers):
    total = evaluate_expression(expression)
    if total is None:
        return False
    if any(total % num == 0 for num in remaining_numbers):
        return False
    return True

def simulate_multiple_times(numbers, num_simulations):
    results = []
    for _ in range(num_simulations):
        largest_number = float('-inf')
        largest_expression = None
        numbers_used = None
        for selected_numbers in combinations(numbers, 6):
            remaining_numbers = [num for num in numbers if num not in selected_numbers]
            if not remaining_numbers:
                continue  # Skip if all numbers are chosen
            simulated_remaining_numbers = []
            for num in remaining_numbers:
                if random.random() < 0.5:  # Simulate approximately half of the remaining numbers
                    simulated_remaining_numbers.append(num)
            if simulated_remaining_numbers:
                for operators in product(['+', '-', '*', '/'], repeat=5):
                    expression = str(selected_numbers[0])
                    for i, op in enumerate(operators):
                        expression += op + str(selected_numbers[i + 1])
                    if is_valid(expression, simulated_remaining_numbers):
                        result = evaluate_expression(expression)
                        if result % 2 != 0:  # Ensure the result is odd
                            if result > largest_number:
                                largest_number = result
                                largest_expression = expression
                                numbers_used = selected_numbers
        results.append((largest_number, largest_expression, numbers_used))
    return results

def plot_highest_numbers(results):
    highest_values = [item[0] for item in results]
    plt.plot(range(1, len(highest_values) + 1), highest_values, marker='o', linestyle='-')
    plt.xlabel('Simulation')
    plt.ylabel('Highest Number Achieved')
    plt.title('Highest Number Achieved in Each Simulation')
    plt.grid(True)
    plt.show()

def main():
    numbers = [2, 3, 4, 5, 6, 7, 8, 9]
    num_simulations = 10
    results = simulate_multiple_times(numbers, num_simulations)
    for i, (highest_number, expression, numbers_used) in enumerate(results, 1):
        print(f"Simulation {i}: Highest Number Achieved:", highest_number)
        print("Expression:", expression)
        print("Numbers Used:", numbers_used)
        print()
    plot_highest_numbers(results)

if __name__ == "__main__":
    main()
