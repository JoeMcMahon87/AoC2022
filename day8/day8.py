import pprint
import numpy as np

def process_input(raw_input: str):
    forest = np.array([[int(el) for el in current_list.strip()] for current_list in raw_input])
    return forest

def get_score(tree_array, tree_index):
    top_array = tree_array[:tree_index[0], tree_index[1]][::-1]
    bottom_array = tree_array[tree_index[0] + 1:, tree_index[1]]
    left_array = tree_array[tree_index[0], :tree_index[1]][::-1]
    right_array = tree_array[tree_index[0], tree_index[1] + 1:]

    top_where = np.where(top_array >= tree_array[tree_index[0], tree_index[1]])[0]
    bottom_where = np.where(bottom_array >= tree_array[tree_index[0], tree_index[1]])[0]
    left_where = np.where(left_array >= tree_array[tree_index[0], tree_index[1]])[0]
    right_where = np.where(right_array >= tree_array[tree_index[0], tree_index[1]])[0]

    top_score = 1 + top_where[0] if top_where.shape[0] != 0 else tree_index[0]
    bottom_score = 1 + bottom_where[0] if bottom_where.shape[0] != 0 else tree_array.shape[0] - tree_index[0] - 1
    left_score = 1 + left_where[0] if left_where.shape[0] != 0 else tree_index[1]
    right_score = 1 + right_where[0] if right_where.shape[0] != 0 else tree_array.shape[1] - tree_index[1] - 1

    return top_score * bottom_score * right_score * left_score

def part_1(data):
    count = 2 * ((data.shape[0] - 1) + (data.shape[1] - 1))
    
    # going from top
    visible_trees = []
    for row in range(1, data.shape[0] - 1):
        current_row = data[row, 1:-1]
        max_heights = np.max(data[:row, 1:-1], axis=0)
        visible_trees.extend([(row, el + 1) for el in np.where(current_row > max_heights)[0]])

    # from down
    for row in range(data.shape[0] - 1, 1, -1):
        current_row = data[row - 1, 1:-1]
        max_heights = np.max(data[row:, 1:-1], axis=0)
        visible_trees.extend([(row - 1, el + 1) for el in np.where(current_row > max_heights)[0]])

    # from left
    for column in range(1, data.shape[1] - 1):
        current_column = data[1:-1, column]
        max_heights = np.max(data[1:-1, :column], axis=1)
        visible_trees.extend([(el + 1, column) for el in np.where(current_column > max_heights)[0]])

    # from right
    for column in range(data.shape[1] - 1, 1, -1):
        current_column = data[1:-1, column - 1]
        max_heights = np.max(data[1:-1, column:], axis=1)
        visible_trees.extend([(el + 1, column - 1) for el in np.where(current_column > max_heights)[0]])

    return count + len(set(visible_trees))

def part_2(data):
    biggest_score = 0
    biggest_index = None
    for i in range(1, data.shape[0] - 1):
        for j in range(1, data.shape[1] - 1):
            cur_index = (i, j)
            cur_score = get_score(data, cur_index)
            if cur_score > biggest_score:
                biggest_score = cur_score
                biggest_index = cur_index
    return biggest_score, biggest_index

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        raw_input = puzzle_input.readlines()

    data = process_input(raw_input)
    ans1 = part_1(data)
    print(ans1)
    ans2 = part_2(data)
    print(ans2)