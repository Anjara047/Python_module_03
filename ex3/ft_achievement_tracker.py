#!/usr/bin/env python3

import random

# 1. Achievement pool (no indentation issue)
all_achievements = [
    "First Steps", "Boss Slayer", "Speed Runner", "World Savior",
    "Untouchable", "Master Explorer", "Collector Supreme", "Strategist",
    "Survivor", "Treasure Hunter", "Sharp Mind", "Unstoppable",
    "Crafting Genius", "Legend", "Night Owl", "Pacifist",
    "Speedster", "Iron Will", "Dragon Slayer", "The Chosen One",
]

def gen_player_achievements() -> set:
    count_pick = random.randint(1, len(all_achievements))
    return set(random.sample(all_achievements, count_pick))


print("=== Achievement Tracker System ===\n")

players = {
    "Alice": gen_player_achievements(),
    "Bob": gen_player_achievements(),
    "Charlie": gen_player_achievements(),
    "Dylan": gen_player_achievements()
}

for name, achieve in players.items():
    print(f"Player {name}: {achieve}")

achievements = set()
for achieve in players.values():
    achievements = achievements.union(achieve)

print("\nAll distinct achievements:", achievements)

common_achievements = None
for achieve in players.values():
    if common_achievements is None:
        common_achievements = achieve
    else:
        common_achievements = common_achievements.intersection(achieve)

print("\nCommon achievements:", common_achievements)
print()

for name, ach in players.items():
    others = set()
    for other_name, other_achieve in players.items():
        if other_name != name:
            others = others.union(other_achieve)
    unique = achieve.difference(others)
    print(f"Only {name} has:", unique)

print()
full_set = set(all_achievements)
for name, achieve in players.items():
    missing = full_set.difference(achieve)
    print(f"{name} is missing:", missing)
