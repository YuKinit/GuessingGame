# Multiplayer Number Guessing Game

This is a simple multiplayer number guessing game implemented in Python using sockets and threading. The game allows multiple players to connect to a server, choose a difficulty level (easy, medium, or hard), and guess a randomly generated number within the specified range.

## Files Included

- `server.py`: Contains the server-side code for managing the game logic, leaderboard, and handling client connections.
- `client.py`: Contains the client-side code for connecting to the server, playing the game, and interacting with the user.

## Installation and Usage

### Prerequisites
- Python 3.x installed on your system.

### Setup
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the downloaded directory.

### Running the Server
1. Open a terminal or command prompt.
2. Navigate to the directory containing `server.py`.
3. Run the command: `python server.py`.
4. The server will start listening for connections on port 12345.

### Running the Client
1. Open a separate terminal or command prompt.
2. Navigate to the directory containing `client.py`.
3. Run the command: `python client.py`.
4. Enter your name when prompted.
5. Choose a difficulty level (easy, medium, or hard).
6. Guess the number as per the hints provided.
7. Play again if desired.

## Leaderboard
The server maintains a leaderboard that ranks players based on their performance. The leaderboard is updated in real-time and displayed periodically.

## Notes
- The server code (`server.py`) should be running before clients can connect and play the game.
- Ensure that the server and client are running on the same machine for local testing.
- Modify the IP address and port in the code if running on a network or different machines.
