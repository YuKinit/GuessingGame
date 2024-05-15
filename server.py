import socket
import random
import threading
import time

leaderboard_file = "leaderboard.txt"
leaderboard = {}

lock = threading.Lock()

def load_leaderboard():
    global leaderboard
    try:
        with open(leaderboard_file, 'r') as file:
            for line in file:
                parts = line.strip().split(': ')
                name = parts[0].split('. ')[1]
                score_text = parts[1]
                score = int(score_text.split()[0])
                leaderboard[name] = score
    except FileNotFoundError:
        pass

def update_leaderboard(name, attempts):
    with lock:
        if name in leaderboard:
            leaderboard[name] = min(leaderboard[name], attempts) 
        else:
            leaderboard[name] = attempts

        with open(leaderboard_file, 'w') as file:
            sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1])  
            sorted_leaderboard.reverse() 
            for rank, (user, score) in enumerate(sorted_leaderboard, start=1):
                file.write(f"{rank}. {user}: {score} attempts\n")


def display_leaderboard():
    with lock:
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1])
        print("\nLeaderboard:")
        for rank, (user, score) in enumerate(sorted_leaderboard, start=1):
            print(f"{rank}. {user}: {score} attempts")
        print()

def refresh_leaderboard():
    while True:
        time.sleep(3)
        display_leaderboard()

def play_game(difficulty):
    if difficulty == 'easy':
        return random.randint(1, 50)
    elif difficulty == 'medium':
        return random.randint(1, 100)
    elif difficulty == 'hard':
        return random.randint(1, 500)

def handle_client(client_socket):
    name = client_socket.recv(1024).decode()
    print(f"Player {name} has joined.")
    
    while True:
        difficulty = client_socket.recv(1024).decode().lower()
        client_socket.send(f"Selected difficulty: {difficulty}".encode())
        
        number_to_guess = play_game(difficulty)
        attempts = 0

        while True:
            guess = int(client_socket.recv(1024).decode())
            attempts += 1
            if guess == number_to_guess:
                client_socket.send("Congratulations! You guessed it right!".encode())
                print(f"{name} guessed the number in {attempts} attempts.")
                update_leaderboard(name, attempts)
                break
            elif guess < number_to_guess:
                client_socket.send("Try guessing higher!".encode())
            else:
                client_socket.send("Try guessing lower!".encode())

        play_again = client_socket.recv(1024).decode().lower()
        if play_again != 'yes':
            print(f"{name} has left the game.")
            break

    client_socket.close()

def main():
    load_leaderboard()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server is listening...")

   
    refresh_thread = threading.Thread(target=refresh_leaderboard, daemon=True)
    refresh_thread.start()

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
