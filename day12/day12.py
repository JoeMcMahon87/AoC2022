import math

max_x = 0
max_y = 0
start_node = None
end_node = None

class Node:
    x = -1
    y = -1
    hgt = 'a'

    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.hgt = h

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def get_neighbors(self):
        global max_x, max_y
        result = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    pass
                elif dx+self.x < 0 or dx+self.x > max_x:
                    pass
                elif dy+self.y < 0 or dy+self.y > max_y:
                    pass
                else:
                    result.append((self.x + dx, self.y + dy))
        return result

    def can_traverse(self, cur_height):
        if ord(cur_height) + 1 <= self.hgt:
            return True
        else:
            return False

    def __repr__(self):
        return '' + self.hgt

    def __str__(self):
        return f"({self.getx()},{self.gety()}) - {self.hgt}"

def process_input(raw_input: str):
    global start_node, end_node, max_x, max_y
    data = []
    x = 0
    y = 0
    for line in raw_input:
        line = line.strip()
        temp = []
        for char in line:
            node = Node(x, y, char)
            x += 1
            if x > max_x:
                max_x = x
            temp.append(node)
            if char == 'S':
                start_node = node
            elif char == 'E':
                end_node = node
        x = 0
        y += 1
        if y > max_y:
            max_y = y
        data.append(temp)
    return data

def iterative_deepening_a_star(start, goal):
    """
    Performs the iterative deepening A Star (A*) algorithm to find the shortest path from a start to a target node.
    Can be modified to handle graphs by keeping track of already visited nodes.
    :param tree:      An adjacency-matrix-representation of the tree where (x,y) is the weight of the edge or 0 if there is no edge.
    :param heuristic: An estimation of distance from node x to y that is guaranteed to be lower than the actual distance. E.g. straight-line distance.
    :param start:      The node to start from.
    :param goal:      The node we're searching for.
    :return: number shortest distance to the goal node. Can be easily modified to return the path.
    """
    # threshold = heuristic[start][goal]
    dist = math.floor(math.sqrt(abs(goal.getx() - start.getx()) ** 2 + abs(goal.getx() - start.getx()) ** 2))

    while True:
        distance = iterative_deepening_a_star_rec(start, goal, 0)
        if distance == float("inf"):
            # Node not found and no more nodes to visit
            return -1
        elif distance < 0:
            # if we found the node, the function returns the negative distance
            print("Found the node we're looking for!")
            return -distance
        else:
            # if it hasn't found the node, it returns the (positive) next-bigger threshold
            dist = distance


def iterative_deepening_a_star_rec(node, goal, distance):
    """
    Performs DFS up to a depth where a threshold is reached (as opposed to interative-deepening DFS which stops at a fixed depth).
    Can be modified to handle graphs by keeping track of already visited nodes.
    :param node:      The node to continue from.
    :param goal:      The node we're searching for.
    :param distance:  Distance from start node to current node.
    :return: number shortest distance to the goal node. Can be easily modified to return the path.
     """
    print("Visiting Node " + str(node))

    if node == goal:
        # We have found the goal node we we're searching for
        return -distance

    print(goal)
    print(node)
    dist = math.floor(math.sqrt(abs(goal.getx() - node.getx()) ** 2 + abs(goal.gety() - node.gety()) ** 2))
    #estimate = distance + dist
    #if estimate > threshold:
    #    print("Breached threshold with heuristic: " + str(estimate))
    #    return estimate

    # ...then, for all neighboring nodes....
    mn = float("inf")
    for neighbor in node.get_neighbors():
        temp = data[neighbor[1]][neighbor[0]]
        t = iterative_deepening_a_star_rec(temp, goal, distance + 1)
        if t < 0:
            # Node found
            return t
        elif t < mn:
            mn = t

    return mn
     
def part_1(data):
    global start_node, end_node
    iterative_deepening_a_star(start_node, end_node)
    return None

def part_2(data):
    return None

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        raw_input = puzzle_input.readlines()

    data = process_input(raw_input)
    print(data)
    ans1 = part_1(data)
    print(f"{ans1}")
    ans2 = part_2(data)
    print(ans2)