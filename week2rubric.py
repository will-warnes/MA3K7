import matplotlib.pyplot as plt
import numpy as np

def print_bracelet_sequence(a, b, max_iterations=200):
    sequence = [(a, b)]
    current_pair = (a, b)

    for iteration in range(1, max_iterations):
        next_number = (current_pair[0] + current_pair[1]) % 10
        current_pair = (current_pair[1], next_number)

        if current_pair in sequence:
            # print(f"Sequence repeated at iteration {iteration}")
            return iteration

        sequence.append(current_pair)

    """
        print("Number Bracelet Sequence:")
        for pair in sequence:
            print(pair)
    """
    

# Example with a = 3, b = 5, and 10
a = 3
b = 5

unique_values=[]
counter=[0,0,0,0,0,0]
for i in range(10):
    for j in range(10):
        temp = (print_bracelet_sequence(i,j))
        if temp not in unique_values:
            unique_values.append(temp)
        
        counter[unique_values.index(temp)] = counter[unique_values.index(temp)] + 1
            
print(f'counter is {counter}')
            



# Create a bar chart
plt.bar(unique_values, counter, color='blue',width=0.8)
plt.xticks(unique_values)

x_values = np.arange(1,61,1)
plt.plot(x_values, x_values, color='red', linestyle='--', label='x=y')

# Add labels and title
plt.xlabel('number of interations in sequence until cycle')
plt.ylabel('number of starting pairs that have sequence')
plt.title('')

# Display the bar chart
plt.show()


print(f'set of values are {unique_values}')
print_bracelet_sequence(a, b)
