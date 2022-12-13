

def read_input():
    lines = None
    with open("input.txt", 'r', encoding="utf-8") as infile:
        lines = infile.readlines()
        process_lines(lines)
    return lines

def process_lines(lines):
    priority = 0

    for i in lines:
        set_a = set()
        set_b = set()
        line = i.strip()
        for j in range(0, len(line)//2):
            set_a.add(line[j])
            set_b.add(line[j + len(line)//2])
        ab = list(set_a.intersection(set_b))[0]
        if ab == ab.lower():
            score = int(ord(ab) - 96)
        else:
            score = int(ord(ab) - 64) + 26

        print(f"{ab} - {score}")
        priority += score

    print(f"{priority}")


def main():

    lines = read_input()

if __name__ == "__main__":
    main()