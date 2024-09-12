#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Labels for the fruits and people
fruits = ['Apples', 'Bananas', 'Oranges', 'Peaches']
people = ['Farrah', 'Fred', 'Felicia']

# Define colors for each fruit
colors = {
    'Apples': 'red',
    'Bananas': 'yellow',
    'Oranges': '#ff8000',
    'Peaches': '#ffe5b4'
}

# Create the bar plot
x = np.arange(len(people))  # the label locations
width = 0.5  # the width of the bars

fig, ax = plt.subplots()
bottoms = np.zeros(len(people))  # to keep track of the bottom of each stack

for i, fruit_type in enumerate(fruits):
    ax.bar(x, fruit[i], width, label=fruit_type, color=colors[fruit_type], bottom=bottoms)
    bottoms += fruit[i]  # update bottoms for the next stack

# Set labels, title, and legend
ax.set_xlabel('People')
ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')
ax.set_xticks(x)
ax.set_xticklabels(people)
ax.set_ylim(0, 80)
ax.set_yticks(np.arange(0, 81, 10))
ax.legend(title='Fruit')

# Show the plot
plt.tight_layout()
plt.show()
