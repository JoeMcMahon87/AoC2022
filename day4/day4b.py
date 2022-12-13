

def read_input():
    lines = None
    with open("input.txt", 'r', encoding="utf-8") as infile:
        lines = infile.readlines()
        process_lines(lines)
    return lines

def process_lines(lines):
    overlapped = 0

    for i in lines:
        line = i.split(",")
        first_set = line[0].split("-")
        second_set = line[1].split("-")
        
        if (int(first_set[0]) == int(second_set[0]) or int(first_set[1]) == int(second_set[1])) or \
           (int(first_set[0]) > int(second_set[0]) and int(first_set[0]) <= int(second_set[1])) or \
           (int(first_set[0]) < int(second_set[0]) and int(first_set[1]) >= int(second_set[0])):
           overlapped += 1
           print(f"{first_set[0]} - {first_set[1]}  {second_set[0]} - {second_set[1]}")
    
    print(f"{overlapped}")


def main():

    lines = read_input()

if __name__ == "__main__":
    main()