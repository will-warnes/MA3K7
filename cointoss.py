import matplotlib.pyplot as plt
def generate_combinations(target, current_combination=[], result=None):
    if result is None:
        result = {}

    if target == 0:
        sequence_length = len(current_combination)
        ends_with = current_combination[-1]
        if sequence_length not in result:
            result[sequence_length] = {'total': 0, 'ends_with_1': 0, 'ends_with_2': 0}
        result[sequence_length]['total'] += 1
        if ends_with == 1:
            result[sequence_length]['ends_with_1'] += 1
        elif ends_with == 2:
            result[sequence_length]['ends_with_2'] += 1
    else:
        if target >= 1:
            generate_combinations(target - 1, current_combination + [1], result)
        if target >= 2:
            generate_combinations(target - 2, current_combination + [2], result)

    return result

def print_results_and_plot(results):
    lengths = list(results.keys())
    totals = [results[length]['total'] for length in lengths]
    ends_with_1 = [results[length]['ends_with_1'] for length in lengths]
    ends_with_2 = [results[length]['ends_with_2'] for length in lengths]

    print("Sequence Length | Total Sequences | Ends with 1 | Ends with 2")
    for length in lengths:
        print(f"{length:<15} | {results[length]['total']:<15} | {results[length]['ends_with_1']:<11} | {results[length]['ends_with_2']}")

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.bar(lengths, totals, color='skyblue', label='Total Sequences')
    plt.bar(lengths, ends_with_1, color='lightgreen', label='Ends with 1')
    plt.bar(lengths, ends_with_2, bottom=ends_with_1, color='salmon', label='Ends with 2')
    plt.xlabel('Sequence Length')
    plt.ylabel('Number of Sequences')
    plt.title('Sequence Length vs. Number of Sequences (Total, Ending in 1, Ending in 2)')
    plt.legend()
    plt.xticks(lengths)
    plt.show()

# Generate combinations for a total of 25
results = generate_combinations(25)

# Print results and plot
print_results_and_plot(results)
