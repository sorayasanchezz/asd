import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")

    # initial list
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    # all capitalized
    capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized}")

    # only already capitalized
    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {capitalized_only}")

    # dict with random scores
    scores = {name: random.randint(0, 1000) for name in capitalized}
    print(f"Score dict: {scores}")

    # average
    avg = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg}")

    # high scores
    high_scores = {name: value for name, value in scores.items() if value > avg}
    print(f"High scores: {high_scores}")
