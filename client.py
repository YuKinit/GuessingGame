import socket

def play_game(client_socket):
    while True:
        guess = int(input("Enter your guess: "))
        client_socket.send(str(guess).encode())
        response = client_socket.recv(1024).decode()
        print(response)
        if "Congratulations" in response:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    name = input("Enter your name: ")
    client_socket.send(name.encode())

    while True:
        difficulty = input("Choose difficulty (easy/medium/hard): ")
        client_socket.send(difficulty.encode())

        response = client_socket.recv(1024).decode()
        print(response)

        play_game(client_socket)

        play_again = input("Play again? (yes/no): ")
        client_socket.send(play_again.encode())
        if play_again.lower() != 'yes':
            break

    client_socket.close()

if __name__ == "__main__":
    main()
