#!/usr/bin/env python3

import random
import typing

player = ["bob", "alice", "dylan", "charlie"]
action = ["run", "eat", "sleep", "grab", "swim", "climb", "release", "move"]


def gen_event() -> typing.Generator[tuple, None, None]:
    while True:
        yield (random.choice(player), random.choice(action))


def ten_event():
    gen = gen_event()
    events = []

    for _ in range(10):
        event = next(gen)
        events.append(event)

    print(f"Built list of 10 events: {events}")
    return (events)


def consume_event(events):
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events.pop(index)
        yield event


def main():
    gen = gen_event()

    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")

    events = ten_event()

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in lists: {events}")


if __name__ == "__main__":
    main()
