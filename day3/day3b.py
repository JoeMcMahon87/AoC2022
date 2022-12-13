

def read_input():
    lines = None
    with open("input.txt", 'r', encoding="utf-8") as infile:
        lines = infile.readlines()
        process_lines(lines)
    return lines

def process_lines(lines):
    priority = 0

    i = 0
    while i<len(lines):
        sets = [set(), set(), set()]
        for group in range(0,3):
            line = lines[i+group].strip()
            for j in range(0, len(line)):
                sets[group].add(line[j])
        temp = list(sets[0].intersection(sets[1]).intersection(sets[2]))[0]

        if temp == temp.lower():
            score = int(ord(temp) - 96)
        else:
            score = int(ord(temp) - 64) + 26

        print(f"{temp} - {score}")
        priority += score
        i += 3

    print(f"{priority}")


def main():

    lines = read_input()

if __name__ == "__main__":
    main()