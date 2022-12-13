from anytree import Node, RenderTree, CountError, PostOrderIter
from anytree.search import find_by_attr

def find_child_node(node, child_name):
    retval = None
    if node.children is not None:
        for child in node.children:
            if child.name == child_name:
                retval = child
                break
    return retval

def process_input(raw_input: str):
    root = Node("/", dirsize=0, objtype="dir")
    cur_node = root
    dirstart = False
    for line in raw_input:
        line = line.strip()
        if line.startswith("$ cd"):
            dirstart = False
            # Process directory change
            parts = line.split(" ")
            dir_name = parts[2].strip()
            if dir_name == '/':
                cur_node = root
                print("Changing to /")
            else:
                if dir_name == '..':
                    cur_node = cur_node.parent
                    print(f"Changing to {cur_node.name}")
                else:
                    print(RenderTree(cur_node))
                    cur_node = find_child_node(cur_node, dir_name)
                    print(f"Changing to {dir_name}")
        elif line.startswith("$ ls"):
            # Process directory listing
            # Nothing to do
            dirstart = True
        else:
            # Directory listing element
            if line.startswith("dir"):
                # subdirectory
                parts = line.split(" ")
                if find_child_node(cur_node, parts[1].strip()) is None:
                    new_node = Node(parts[1].strip(), parent=cur_node, dirsize=0, objtype="dir")
                    print(f"Adding dir: {parts[1].strip()}")
            else:
                # individual file
                parts = line.split(" ")
                if find_child_node(cur_node, parts[1].strip()) is None:
                    new_node = Node(parts[1].strip(), parent=cur_node, dirsize=int(parts[0].strip()), objtype="file")
                    print(f"Adding file: {parts[1].strip()}")

    return root

def calculate_sizes(node) -> int:
    size = 0
    print(f"{node.name} ({node.objtype}) - {node.dirsize}")
    if node.objtype == "dir":
        # Sum up children sizes
        if node.children is not None:
            for child in node.children:
                size += calculate_sizes(child)
            node.dirsize = size
    else:
        size = node.dirsize

    return size

def part_1(root):
    result = 0
    print(RenderTree(root))
    total_size = calculate_sizes(root)  
    
    for x in PostOrderIter(root):
        if x.objtype == "dir" and x.dirsize <= 100000:
            result += x.dirsize

    return result

def part_2(root):
    total_size = root.dirsize
    size_required = 30000000
    cur_size = 70000000
    size_needed = size_required - (70000000 - total_size)

    print(f"{size_needed}")
    for x in PostOrderIter(root):
        if x.objtype == "dir" and x.dirsize >= size_needed and x.dirsize <= cur_size:
            cur_size = x.dirsize
    return cur_size

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        raw_input = puzzle_input.readlines()

    root = process_input(raw_input)
    ans1 = part_1(root)
    print(ans1)
    ans2 = part_2(root)
    print(ans2)