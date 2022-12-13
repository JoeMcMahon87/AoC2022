

def read_input():
    lines = None
    with open("input.txt", 'r', encoding="utf-8") as infile:
        lines = infile.readlines()
        process_lines(lines)
    return lines

def process_lines(lines):
    cur_total = 0
    max_total = 0
    selected = 0
    cur_target = 1
    
    elves = []
    for i in lines:
        line = i.strip()
        if len(line) > 0:
            cals = int(line)
            cur_total += cals
        else:
            elf = (cur_target, cur_total)
            elves.append(elf)
            cur_target += 1
            cur_total = 0

    elves.sort(key=lambda y: y[1], reverse=True)
    print(elves)
    print(elves[0][1] + elves[1][1] + elves[2][1])

def main():

    lines = read_input()

if __name__ == "__main__":
    main()