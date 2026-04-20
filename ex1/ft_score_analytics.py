#! /usr/bin/env python3

import sys

def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")

    argc = len(sys.argv)

    if argc == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    scores = []
    i = 1

    while i < argc:
        arg = sys.argv[i]
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
        i += 1

    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return

    total_players = len(scores)
    total_score = sum(scores)
    average_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    ft_score_analytics()
