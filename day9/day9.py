visited = set()
min_x = 3000
min_y = 3000
max_x = 0
max_y = 0

def process_input(raw_input: str):
    return raw_input

def print_map(head, tail):
    output = ''
    for y in range(4,-1, -1):
        for x in range(0,6):
            temp = (x+1000, y+1000)
            if temp == head:
                output += 'H'
            elif temp == tail:
                output += 'T'
            elif temp in visited:
                output += '#'
            else:
                output += '.'
        output += '\n'
    print(output)

def move_tail(head, tail):
    found = False
    for dx in range(-1,2):
        for dy in range(-1,2):
            if tail[0]+dx == head[0] and tail[1]+dy == head[1]:
                found = True
                break
    tail_x = tail[0]
    tail_y = tail[1]
    if not found:
        if head[0] < tail[0]:
            tail_x -= 1
        elif head[0] > tail[0]:
            tail_x += 1
        if head[1] < tail[1]:
            tail_y -= 1
        elif head[1] > tail[1]:
            tail_y += 1
    
    visited.add((tail_x, tail_y))
    # print_map(head, (tail_x, tail_y))
    return tail_x, tail_y

def move_rope(head, tail, rope_length):
    global min_x, min_y, max_x, max_y
    found = False
    cur = head
    for i in range(1,rope_length+1):
        for dx in range(-1,2):
            for dy in range(-1,2):
                if tail[i][0]+dx == cur[0] and tail[i][1]+dy == cur[1]:
                    found = True
                    break
        tail_x = tail[i][0]
        tail_y = tail[i][1]
        if not found:
            #print(f"Move part {i} of rope")
            if cur[0] < tail[i][0]:
                tail_x -= 1
            elif cur[0] > tail[i][0]:
                tail_x += 1
            if cur[1] < tail[i][1]:
                tail_y -= 1
            elif cur[1] > tail[i][1]:
                tail_y += 1

            if tail_x < min_x:
                min_x = tail_x
            if tail_x > max_x:
                max_x = tail_x
            if tail_y < min_y:
                min_y = tail_y
            if tail_y > max_y:
                max_y = tail_y

            tail[i] = (tail_x, tail_y)
#        else:
#            print(f"Rope part {i} stays")
        cur = tail[i]

    #print_rope(head, tail, rope_length)
    visited.add((tail[rope_length][0], tail[rope_length][1]))

def print_rope(head, tail, rope_length):
    output = ''
    for y in range(max_y + 1, min_y - 2, -1):
        for x in range(min_x - 1, max_x + 2):
            temp = (x, y)
            square = '.'
            for i in range(rope_length, 0, -1):
                if tail[i] == temp:
                    square = str(i)
            if temp == head:
                square = 'H'
            elif square == '.' and temp in visited:
                square = '#'
            output += square
        output += '\n'
    print(output)

def part_1(data):
    head_x = 1000
    head_y = 1000
    tail_x = 1000
    tail_y = 1000
    for line in data:
        directions = line.split(" ")
        if directions[0] == 'U':
            for i in range(0, int(directions[1])):
                head_y += 1
                tail_x, tail_y = move_tail((head_x, head_y), (tail_x, tail_y))
        elif directions[0] == 'D':
            for i in range(0, int(directions[1])):
                head_y -= 1
                tail_x, tail_y = move_tail((head_x, head_y), (tail_x, tail_y))
        elif directions[0] == 'L':
            for i in range(0, int(directions[1])):
                head_x -= 1
                tail_x, tail_y = move_tail((head_x, head_y), (tail_x, tail_y))
        elif directions[0] == 'R':
            for i in range(0, int(directions[1])):
                head_x += 1
                tail_x, tail_y = move_tail((head_x, head_y), (tail_x, tail_y))

    return len(visited)

def part_2(data):
    visited.clear()
    head_x = 1000
    head_y = 1000
    rope_length = 9
    tail = {}
    for i in range(1, rope_length+1):
        tail[i] = (1000, 1000)

    for line in data:
        directions = line.split(" ")
        if directions[0] == 'U':
            for i in range(0, int(directions[1])):
                head_y += 1
                move_rope((head_x, head_y), tail, rope_length)
        elif directions[0] == 'D':
            for i in range(0, int(directions[1])):
                head_y -= 1
                move_rope((head_x, head_y), tail, rope_length)
        elif directions[0] == 'L':
            for i in range(0, int(directions[1])):
                head_x -= 1
                move_rope((head_x, head_y), tail, rope_length)
        elif directions[0] == 'R':
            for i in range(0, int(directions[1])):
                head_x += 1
                move_rope((head_x, head_y), tail, rope_length)

    print_rope((head_x, head_y), tail, rope_length)
    return len(visited)

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        raw_input = puzzle_input.readlines()

    data = process_input(raw_input)
    ans1 = part_1(data)
    print(ans1)
    ans2 = part_2(data)
    print(ans2)