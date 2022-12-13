reg_x = {}

def process_input(raw_input: str):
    global reg_x
    cycle = 0
    reg_x[0] = 1
    for line in raw_input:
        cycle += 1
        if line.startswith("noop"):
            reg_x[cycle] = reg_x[cycle - 1]
            print(f"{cycle:03d}:{line.strip()}\t{reg_x[cycle]}")
        else:
            inst = line.split(" ")
            delta = int(inst[1])

            reg_x[cycle] = reg_x[cycle - 1]
            print(f"{cycle:03d}:{line.strip()}\t{reg_x[cycle]}")
            cycle += 1
            reg_x[cycle] = reg_x[cycle - 1] + delta
            print(f"{cycle:03d}:{line.strip()}\t{reg_x[cycle]}")

    return cycle
    
def part_1(max_cycle):
    global reg_x
    interesting_cycles = [19, 59, 99, 139, 179, 219]
    signal_strength = 0
    for i in range(1, max_cycle + 1):
        if i in interesting_cycles:
            print(f"Cycle {i+1} - Register X: {reg_x[i]}")
            signal_strength += ((i+1) * reg_x[i])

    return signal_strength

def part_2():
    global reg_x
    crt = ''
    current_pixel = 0
    
    for i in range(1, max_cycle + 1):
        if max(current_pixel - 1, 1) <= reg_x[i-1] and reg_x[i-1] <= min(current_pixel + 1, max_cycle):
            crt += str('#')
        else:
            crt += str('.')
        if i % 40 == 0:
            crt += '\n'
        current_pixel += 1
        if current_pixel % 40 == 0:
            current_pixel = 0

    return crt

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        raw_input = puzzle_input.readlines()

    max_cycle = process_input(raw_input)
    ans1 = part_1(max_cycle)
    print(f"{ans1}")
    ans2 = part_2()
    print(ans2)