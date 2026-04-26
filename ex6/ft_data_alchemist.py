#!/usr/bin/env python3

import random


players = ["Alice", "bob", "Charlie", "dylan",
           "Emma", "Gregory", "john", "kevin", "Lian"]


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")

    print(f"Initial list of players: {players}")

    name_capitalized = [player.capitalize() for player in players]
    print(f"\nNew list with all names capitalized: {name_capitalized}")

    capitalized_only = [player for player in players if player[0].isupper()]
    print(f"\nNew list of capitalized names only: {capitalized_only}")

    scores = {player: random.randint(1, 1000) for player in name_capitalized}
    print(f"\nScore dict: {scores}")

    average = sum(scores.values()) / len(scores)
    print(f"\nScore Average: {round(average, 2)}")

    high_score = {
        player: score
        for player, score in scores.items()
        if score > average
    }
    print(f"\nHigh scores: {high_score}")


if __name__ == "__main__":
    ft_data_alchemist()
