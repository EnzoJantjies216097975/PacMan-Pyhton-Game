# Pac-Man Python Game

![readme.png](assets%2Freadme.png)
##  Table of Contents

  -  [About the Project]
  -  [Features]
  -  [Installation]
  -  [Usage]
  -  [Game Mechanics]
  -  [How to Play]
  -  [Project Structure]
  -  [Technologies Used]
  -  [Contributing]
  -  [License]
  -  [Contact]


## About the Project

The Pac-Man Python Game is a modern rendition of the classic arcade game, developed using Python and Pygame. This project aims to replicate the gameplay of the original Namco Pac-Man game, including unique ghost behaviors, animations, and challenging maze navigation.


## Features

- <b>Fully functional game mechanics</b> with player control and ghost AI.
- <b>Animation and Sound Effects:</b> Authentic sound effects and animations for an immersive experience.
- <b>Maze Design:</b> Uses 8x8 px tiles to create the maze, allowing for customizable layouts.
- <b>Collision Detection</b> for walls and ghost interactions.
- <b>Score Tracking</b> and levels.


## Installation

   1. <b>Clone the repository:</b>

```bash
git clone https://github.com/yourusername/pacman-python-game.git
 
cd pacman-python-game
```

  2. <b>Install dependencies:</b> Ensure you have Python installed. Install pygame via:

```bash
pip install pygame
```

3.  Run the game:
```bash
python main.py
````


## Usage

- Run main.py to start the game.
- Control Pac-Man using the arrow keys on your keyboard.
- Collect all the pellets and avoid the ghosts to progress through levels.


## Game Mechanics

- <b>Player Movement:</b> Move Pac-Man through the maze using the arrow keys.
- <b>Ghost AI:</b> Ghosts move strategically and have different behaviors. 
- <b>Power-Ups:</b> Eat power pellets to temporarily turn the tables and chase the ghosts.
- <b>Teleportation:</b> Use pathways to move from one side of the maze to the other. 
- <b>Game Over:</b> The game ends when Pac-Man loses all lives.


## How to Play

- <b>Objective:</b> Collect all the dots in the maze while avoiding the ghosts.
- <b>Controls:</b>
  - <b>Arrow Keys:</b> Navigate Pac-Man through the maze.
- <b>Scoring:</b>
  - <b>Pellets:</b> +10 points each.
  - <b>Power Pellets:</b> +50 points and enables ghost chasing for a short period.
  - <b>Ghosts (when powered up):</b> +200 points each (increases with consecutive captures).


## Project Structure

```
PacMan-Python-Game/\
│
├── assets/              # Game assets such as images and sound
├── ghosts/ 
│   ├── pacman/ 
│   └── tiles/ 
│ 
├── main.py              # Main game loop 
├── ghost.py             # Ghost class and logic 
├── pacman.py            # Pac-Man player logic 
├── settings.py          # Game settings and constants
└── world.py             # World/maze generation and wall collision logic
```


## Technologies Used

- Python 3.12.7
- Pygame 1.9.1  (for game development)


## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project.
2. Create a feature branch (git checkout -b feature/new-feature).
3. Commit your changes (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature/new-feature).
5. Open a pull request.


## License

This project is licensed under the MIT License.


# Contact

Enzo Jantjies

- <b>GitHub:</b> @EnzoJantjies216097975
- <b>Email:</b> enzojantjies@gmail.com
