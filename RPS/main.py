import random

# Global valid moves
moves = ['rock', 'paper', 'scissors']


# Helper function to check which move beats the other
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Base Player class
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# HumanPlayer class
class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move (rock, paper, scissors): ").lower()
            if move in moves:
                return move
            print("Invalid move. Try again!")


# RandomPlayer class
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# ReflectPlayer class
class ReflectPlayer(Player):
    def __init__(self):
        self.their_last_move = None

    def move(self):
        if self.their_last_move:
            return self.their_last_move
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_last_move = their_move


# CyclePlayer class
class CyclePlayer(Player):
    def __init__(self):
        self.last_move = None

    def move(self):
        if self.last_move is None:
            self.last_move = random.choice(moves)
        else:
            index = (moves.index(self.last_move) + 1) % len(moves)
            self.last_move = moves[index]
        return self.last_move

    def learn(self, my_move, their_move):
        pass


# Game class
class Game:
    def __init__(self, p1, p2, rounds=3):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.rounds = rounds

    def play_round(self, round_num):
        print(f"\nRound {round_num}:")
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played: {move1}")
        print(f"Opponent played: {move2}")

        if beats(move1, move2):
            self.p1_score += 1
            print("You win the round!")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Opponent wins the round!")
        else:
            print("It's a tie!")

        print(f"Score - You: {self.p1_score} | Opponent: {self.p2_score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("🪨📄✂️ Let's play Rock, Paper, Scissors!")
        for round_num in range(1, self.rounds + 1):
            self.play_round(round_num)
        print("\n🎉 Game Over! Final Score:")
        print(f"You: {self.p1_score} | Opponent: {self.p2_score}")
        if self.p1_score > self.p2_score:
            print("🏆 You win the game!")
        elif self.p2_score > self.p1_score:
            print("💻 Opponent wins the game!")
        else:
            print("🤝 It's a tie!")


# Choose your opponent
def select_opponent():
    print("\nChoose your opponent:")
    print("1. RockPlayer (always plays rock)")
    print("2. RandomPlayer (plays randomly)")
    print("3. ReflectPlayer (copies your last move)")
    print("4. CyclePlayer (cycles through moves)")
    while True:
        choice = input("Enter number (1-4): ")
        if choice == '1':
            return Player()
        elif choice == '2':
            return RandomPlayer()
        elif choice == '3':
            return ReflectPlayer()
        elif choice == '4':
            return CyclePlayer()
        else:
            print("Invalid choice. Try again!")


if __name__ == '__main__':
    opponent = select_opponent()
    rounds = input("\nHow many rounds would you like to play? ")
    if not rounds.isdigit() or int(rounds) <= 0:
        rounds = 3
        print("Invalid input. Defaulting to 3 rounds.")
    else:
        rounds = int(rounds)

    game = Game(HumanPlayer(), opponent, rounds)
    game.play_game()
