
import random
import numpy as np # type: ignore

# Problem Parameters
NUM_ITEMS = 10  # Number of items
BIN_CAPACITY = 15  # Capacity of each bin
POP_SIZE = 20  # Population size
NUM_GENERATIONS = 100  # Maximum generations
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.2

# Generate random item sizes
item_sizes = np.random.randint(1, 10, NUM_ITEMS)

# Initialize population
def initialize_population():
    return [np.random.randint(0, NUM_ITEMS, NUM_ITEMS) for _ in range(POP_SIZE)]

# Fitness function (Minimizing Number of Bins Used)
def fitness(chromosome):
    bins = []
    for item in chromosome:
        placed = False
        for bin in bins:
            if sum(bin) + item_sizes[item] <= BIN_CAPACITY:
                bin.append(item_sizes[item])
                placed = True
                break
        if not placed:
            bins.append([item_sizes[item]])
    return len(bins)  # Minimize bin count

# Selection (Roulette Wheel Selection)
def selection(population):
    fitness_values = np.array([1 / (1 + fitness(ch)) for ch in population])  # Inverse for minimization
    probabilities = fitness_values / fitness_values.sum()
    selected_indices = np.random.choice(len(population), size=2, p=probabilities)
    return population[selected_indices[0]], population[selected_indices[1]]

# Crossover (One-Point Crossover)
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, NUM_ITEMS - 1)
        child1 = np.concatenate((parent1[:point], parent2[point:]))
        child2 = np.concatenate((parent2[:point], parent1[point:]))
        return child1, child2
    return parent1, parent2

# Mutation (Swapping Items)
def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(NUM_ITEMS), 2)
        chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome

# Genetic Algorithm Execution
population = initialize_population()
for generation in range(NUM_GENERATIONS):
    new_population = []
    for _ in range(POP_SIZE // 2):
        parent1, parent2 = selection(population)
        child1, child2 = crossover(parent1, parent2)
        new_population.extend([mutate(child1), mutate(child2)])
    population = sorted(new_population, key=fitness)[:POP_SIZE]  # Keep best solutions

# Best solution found
best_solution = min(population, key=fitness)
best_fitness = fitness(best_solution)
print("Best Packing Arrangement:", best_solution)
print("Minimum Number of Bins Used:", best_fitness)