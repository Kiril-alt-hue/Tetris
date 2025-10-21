# Pygame Tetris

This is a classic Tetris game implemented in Python using the Pygame library. The project includes complete game logic, sound management, theme selection, score tracking, and a timer.

## 🌟 Key Features

  * **Main Menu:** An interactive menu to select a theme (Classic or Pink) and exit the game.
  * **Sound Management:** A complete `SoundManager` for background music in the menu and game, as well as sound effects for piece drops and line clears.
  * **Game Logic:**
      * Full implementation of the 7 classic Tetris shapes (I, O, T, S, Z, J, L).
      * Mechanics for piece rotation, movement, and "soft" dropping.
      * "Hard Drop" functionality by pressing `Space`.
      * Collision detection with walls, the floor, and other pieces.
      * Clearing completed lines and scoring points.
      * Displaying the next upcoming piece.
  * **Interface and Rendering:**
      * Rendering the game board, grid, and the falling piece.
      * A separate UI platform to display the score, timer, and next piece.
      * A "Game Over" screen showing the final score, time, and options to restart or return to the menu.
      * Pause functionality (via the `P` key).
  * **Timer:** An in-game timer that tracks the total session time.

## 🎮 How to Play

  * **Piece Movement:**
      * `◄` (Left Arrow): Move left-down (diagonal).
      * `►` (Right Arrow): Move right-down (diagonal).
      * `▼` (Down Arrow): Speed up the fall (soft drop).
  * **Rotation and Dropping:**
      * `▲` (Up Arrow): Rotate the piece.
      * `Space`: Instantly drop the piece (hard drop).
  * **Game Control:**
      * `P`: Pause/unpause the game.
  * **Game Over Screen:**
      * `R`: Restart the game.
      * `M`: Return to the main menu.

## 🛠️ Installation and Setup

To run the game, you will need Python and the `pygame` library.

1.  **Clone the repository:**

    ```bash
    git clone https://your-github-repo-url/pygame-tetris.git
    cd pygame-tetris
    ```

2.  **Install dependencies:**
    You will most likely only need `pygame`.

    ```bash
    pip install pygame
    ```

3.  **Run the game:**
    The main entry point is `main.py`.

    ```bash
    python main.py
    ```

## 📂 Project Structure

The project has a clean structure that separates logic (core), rendering (view), and mechanics (mechanika).

```
Tetris/
├── Board.py             # Game board logic (collisions, line clearing)
├── Piece.py             # Classes for all game pieces and their behavior
├── main.py              # Main file, game loop
├── mechanika/
│   ├── KeyHoldHandler.py  # Handles continuous key presses (movement)
│   └── KeyPressHandler.py # Handles single key presses (rotation, pause)
├── view/
│   ├── Button.py          # Class for menu buttons
│   ├── DrawBoard.py       # Renders the "locked" pieces on the board
│   ├── DrawPauseOnOff.py  # Render manager (game/pause)
│   ├── DrawPiece.py       # Renders the falling piece
│   ├── DrawScore.py       # Renders the score
│   ├── DrawTimer.py       # Renders the timer
│   ├── GameOverScreen.py  # Game Over screen
│   ├── Grid.py            # Renders the game grid
│   ├── Platform.py        # Renders the bottom UI panel
│   └── icon.png           # Window icon
├── gameMain/
│   ├── SpawnPiece.py      # Logic for creating new and next pieces
│   ├── ThemeSelection.py  # Main menu and theme selection class
│   └── Timer.py           # Timer logic
├── sound/
│   ├── SoundManager.py    # Manager for loading and playing sounds
│   ├── menu_track.mp3     # Music
│   ├── game_tracks/       # In-game music
│   │   ├── track1.mp3
│   │   ├── track2.mp3
│   │   └── track3.mp3
│   ├── drop.wav           # Sound effects
│   ├── clear.wav
│   └── game_over.mp3
└── fonts/
    └── jokerman.ttf       # Font for UI
```
