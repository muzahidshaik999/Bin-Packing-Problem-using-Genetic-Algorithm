# Bin Packing Problem using Genetic Algorithm

## Problem Statement
The Bin Packing Problem involves assigning a set of items with specific sizes to a set of bins with a fixed capacity. The objective is to find an optimal arrangement of items into bins such that the number of bins used is minimized. This problem has applications in resource allocation, logistics, and packing industries.

## Genetic Algorithm Approach
### 1. **Chromosome Representation**
Each chromosome represents a possible packing arrangement of items into bins. The genes within a chromosome indicate how items are assigned to bins.

### 2. **Fitness Function**
The fitness function evaluates the quality of a solution by counting the number of bins used. A lower bin count indicates a better solution. Overfilled bins are penalized to encourage feasible packing.

### 3. **Genetic Operators**
#### **Selection (Roulette Wheel Selection)**
- Selects two parent chromosomes based on their fitness scores.
- The probability of selection is inversely proportional to the number of bins used (fewer bins is better).

#### **Crossover (One-Point Crossover)**
- A crossover point is randomly selected.
- Genes after the crossover point are swapped between two parents to generate offspring.
- The crossover ensures that bin constraints are respected.

#### **Mutation (Swapping Items)**
- Randomly selects two items and swaps them between bins.
- Ensures that the feasibility of the solution is maintained while introducing diversity in the population.

### 4. **Algorithm Execution**
1. **Initialization:** Generate an initial population of packing solutions.
2. **Genetic Operations:** Apply selection, crossover, and mutation to create new solutions.
3. **Termination Condition:** The algorithm stops when the maximum number of generations is reached or an optimal packing arrangement is found.

## Implementation Details
- **Number of Items:** 10
- **Bin Capacity:** 15
- **Population Size:** 20
- **Generations:** 100
- **Crossover Rate:** 0.8
- **Mutation Rate:** 0.2
- **Item Sizes:** Randomly generated within a range (1-10)

## Output
The algorithm outputs:
- The best packing arrangement found.
- The minimum number of bins required to store all items efficiently.

## Requirements
- Python 3
- NumPy

## Usage
Run the Python script to execute the Genetic Algorithm and find the optimal bin packing solution.

```sh
python bin_packing_ga.py
```

## Example Output
```
Best Packing Arrangement: [2 1 0 3 2 1 4 0 1 3]
Minimum Number of Bins Used: 4
```

This indicates that each item is assigned to a specific bin, and the optimal arrangement minimizes the number of bins used.

