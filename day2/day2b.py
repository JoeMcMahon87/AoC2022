ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

rock_score = 1
paper_score = 2
scissors_score = 3

win_score = 6
draw_score = 3
lose_score = 0

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
        needed_outcome = line[1]
        outcome = 0
        move = 0
        if opponent_move == ROCK:
            if needed_outcome == LOSE:
                outcome = lose_score
                move = scissors_score
            elif needed_outcome == DRAW:
                outcome = draw_score
                move = rock_score
            elif needed_outcome == WIN:
                outcome = win_score
                move = paper_score
        elif opponent_move == PAPER:
            if needed_outcome == LOSE:
                outcome = lose_score
                move = rock_score
            elif needed_outcome == DRAW:
                outcome = draw_score
                move = paper_score
            elif needed_outcome == WIN:
                outcome = win_score
                move = scissors_score
        elif opponent_move == SCISSORS:
            if needed_outcome == LOSE:
                outcome = lose_score
                move = paper_score
            elif needed_outcome == DRAW:
                outcome = draw_score
                move = scissors_score
            elif needed_outcome == WIN:
                outcome = win_score
                move = rock_score

        score += (move + outcome)
    
    print(f"{score}")

def main():

    lines = read_input()

if __name__ == "__main__":
    main()