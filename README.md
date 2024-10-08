# Voter Model Simulation

This repository contains Python code for simulating the Voter Model with a specified number of votes and lattice size, along with a probability of flipping votes.

## Introduction

The Voter Model is a stochastic model used to describe the evolution of opinion or state among a population of individuals. In this simulation, each cell in a lattice represents an individual, and their vote can evolve based on the votes of their neighbors.

## Getting Started

To run the simulation, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the required dependencies by running:
```bash
pip install numpy matplotlib seaborn
```
4. Run the script `voter_model.py`:

```bash
python voter_model.py
```

## Code Structure
The code consists of the following main parts:

* initial_state(v, N): Initializes the lattice with random votes.
* checkflip(r, c, lattice, p, N): Checks if the vote at a given position should flip based on a probability.
* magnetization(lattice, N): Calculates the magnetization of the lattice, i.e., the number of maximum votes.
* step(lattice, N, p, nstep): Simulates the Voter Model for a given number of steps.

## Parameters
* v: Number of votes.
* N: Number of cells in the lattice.
* p: Probability of accepting flipping a vote.
* nstep: Number of simulation steps.

## Visualization
The simulation is visualized using Matplotlib's animation capabilities. Each frame represents a step in the simulation, displaying the updated state of the lattice along with the magnetization.
