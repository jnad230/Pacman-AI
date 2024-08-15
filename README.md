# Pacman AI Agent

This project implements an AI agent for the classic game of Pacman (as provided by UC Berkeley's CS188 Intro to AI course), using various search algorithms to navigate mazes and avoid ghosts.

## Project Description

The Pacman AI agent uses the following algorithms:
- A* search for efficient pathfinding to collect food dots
- Alpha-Beta pruning for adversarial search in ghost avoidance
- Custom evaluation functions for multi-ghost environments

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/jnad230/Pacman-AI.git
   ```
2. Navigate to the project directory:
   ```
   cd Pacman-AI
   ```
3. Ensure you have Python installed (version 3.6 or higher recommended)

## Usage

Run the main script with:

```
python pacman.py
```

Different algorithms can be tested using command-line arguments. For example:

```
python pacman.py -l mediumClassic -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

## Performance

The implemented algorithms show significant improvements over baseline implementations:
- Up to 800% score increase in classic maze layouts
- Efficient ghost avoidance in complex scenarios

## Contributing

Contributions to improve the AI agent or extend its capabilities are welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is open source, under the [MIT license](LICENSE).
