import queue
from functools import reduce

def process_input(raw_input: str):
    print(raw_input)

def part_1(raw_input):
    q = []
    position = 0

    while len(q) < 4:
        q.append(raw_input[position])
        position += 1
    
    set_len = len(set(q))
    while (set_len < 4):
        q.pop(0)
        q.append(raw_input[position])
        position += 1
        set_len = len(set(q))

    print(f"{q} {position}")
    return position

def part_2(raw_input):
    q = []
    position = 0

    while len(q) < 14:
        q.append(raw_input[position])
        position += 1
    
    set_len = len(set(q))
    while (set_len < 14):
        q.pop(0)
        q.append(raw_input[position])
        position += 1
        set_len = len(set(q))

    print(f"{q} {position}")
    return position

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        raw_input = puzzle_input.read()

    process_input(raw_input)
    ans1 = part_1(raw_input)
    print(ans1)
    ans2 = part_2(raw_input)
    print(ans2)