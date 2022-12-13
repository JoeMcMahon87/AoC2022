

def read_input():
    lines = None
    with open("input.txt", 'r', encoding="utf-8") as infile:
        lines = infile.readlines()
        process_lines(lines)
    return lines

def process_lines(lines):
    score = 0

    for i in lines:
        line = i.strip().split(" ")
        opponent_move = line[0]
        my_move = line[1]
        outcome = 0
        move = 0
        if opponent_move == 'A':
            if my_move == 'X':
                outcome = 3
                move = 1
            elif my_move == 'Y':
                outcome = 6
                move = 2
            elif my_move == 'Z':
                outcome = 0
                move = 3
        elif opponent_move == 'B':
            if my_move == 'X':
                outcome = 0
                move = 1
            elif my_move == 'Y':
                outcome = 3
                move = 2
            elif my_move == 'Z':
                outcome = 6
                move = 3
        elif opponent_move == 'C':
            if my_move == 'X':
                outcome = 6
                move = 1
            elif my_move == 'Y':
                outcome = 0
                move = 2
            elif my_move == 'Z':
                outcome = 3
                move = 3

        score += (move + outcome)
    
    print(f"{score}")

def main():

    lines = read_input()

if __name__ == "__main__":
    main()