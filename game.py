import mysql.connector
import random

class Minesweeper:
    def __init__(self, n=5, m=2):
        self.n = n
        self.m = m
        self.grid = [['-' for _ in range(n)] for _ in range(n)]  # Initialize all tiles as unturned
        self.mines = set()
        self.remaining_tiles = n * n

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.m:
            x, y = random.randint(0, self.n - 1), random.randint(0, self.n - 1)
            if (x, y) not in self.mines:
                self.mines.add((x, y))
                mines_placed += 1

    def print_grid(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.grid[i][j], end=" ")
            print()

    def check_tile(self, index):
        x = (index - 1) // self.n
        y = (index - 1) % self.n
        if (x, y) in self.mines:
            self.grid[x][y] = '0'
            return False
        else:
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (0 <= x + dx < self.n) and (0 <= y + dy < self.n) and (dx != 0 or dy != 0):
                        if (x + dx, y + dy) in self.mines:
                            count += 1
            self.grid[x][y] = str(count) if count > 0 else '1'
            self.remaining_tiles -= 1
            return True

    def store_grid_state_in_mysql(self):
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="joshi",
            password="alala",
            database="results"
        )
        cursor = connection.cursor()

        # Insert grid state into MySQL table
        for x in range(self.n):
            for y in range(self.n):
                cursor.execute("INSERT INTO grid_state (x, y, value) VALUES (%s, %s, %s)", (x, y, self.grid[x][y]))

        # Commit changes and close connection
        connection.commit()
        connection.close()

    def play(self):
        print("Welcome to Minesweeper!")
        print("Player 1 starts.")
        while True:
            print("Remaining tiles:", self.remaining_tiles)
            self.print_grid()
            index = int(input("Enter index (1 to {}): ".format(self.n * self.n)))
            if not (1 <= index <= self.n * self.n):
                print("Invalid index! Please enter a number between 1 and {}.".format(self.n * self.n))
                continue
            if not self.check_tile(index):
                print("Player 1 hits a mine! Player 1 loses!")
                break
            if self.remaining_tiles == self.m:
                print("All non-mine tiles revealed! It's a draw!")
                break

            print("Player 2's turn.")
            print("Remaining tiles:", self.remaining_tiles)
            self.print_grid()
            index = int(input("Enter index (1 to {}): ".format(self.n * self.n)))
            if not (1 <= index <= self.n * self.n):
                print("Invalid index! Please enter a number between 1 and {}.".format(self.n * self.n))
                continue
            if not self.check_tile(index):
                print("Player 2 hits a mine! Player 2 loses!")
                break
            if self.remaining_tiles == self.m:
                print("All non-mine tiles revealed! It's a draw!")
                break

        print("\nFinal state of the grid:")
        for x in range(self.n):
            for y in range(self.n):
                if (x, y) in self.mines:
                    self.grid[x][y] = '0'
        self.print_grid()

        # Store final grid state in MySQL
        self.store_grid_state_in_mysql()

if __name__ == "__main__":
    game = Minesweeper(n=5, m=2)
    game.place_mines()
    game.play()
