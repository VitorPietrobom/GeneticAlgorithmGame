# Genetic Algorithm Game


## Introduction

This repository contains a simple game called Points Collector, implemented using the Pygame library in Python. The game's objective is to collect green points while avoiding red enemies. The player controls a blue square using arrow keys to navigate the screen.
My key objective with this is to test and learn about genetic algorithms implementations


## Features

- Player-controlled movement using arrow keys.
- Random spawning of green points and red enemies.
- Score tracking, where points increase the score and enemies decrease it.
- Screen boundaries to keep the player and objects within the visible area.

## Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/VitorPietrobom/GeneticAlgorithmGame.git
   ```

2. Navigate to the project directory:

   ```bash
   cd GeneticAlgorithmGame
   ```

3. Install Pygame:

   ```bash
   pip install pygame
   ```

### Usage

1. Run the game:

   ```bash
   python main.py
   ```

2. Use the arrow keys to control the blue square.
3. Collect green points to increase your score.
4. Avoid red enemies, as they will decrease your score.
5. The game ends when the score becomes negative.

## Customization

You can customize various aspects of the game by modifying the following variables in the `main.py` file:

- `MIN_VELOCITY` and `MAX_VELOCITY`: Control the speed range of points and enemies.
- `PLAYER_SPEED`: Adjust the speed of the player-controlled square.
- `POINTS_SPAWN_RATE` and `ENEMIES_SPAWN_RATE`: Determine the spawn rate of points and enemies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

