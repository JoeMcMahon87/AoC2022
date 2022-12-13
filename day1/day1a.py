

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
    
    for i in lines:
        line = i.strip()
        if len(line) > 0:
            cals = int(line)
            cur_total += cals
        else:
            if cur_total > max_total:
                max_total = cur_total
                selected = cur_target
            cur_target += 1
            cur_total = 0

    print(f"{selected} has most cals at {max_total}")

def main():

    lines = read_input()

if __name__ == "__main__":
    main()