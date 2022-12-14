monkeys = {}

from tqdm import tqdm

class Item:
    def __init__(self,
                 initial_value: int):
        self.value = initial_value
        self.divisible_by = {i: self.value % i for i in [2, 3, 5, 7, 11, 13, 17, 19, 23]}

    def get_value(self):
        return self.value

    def update_divisible_by_on_add(self, add_value):
        for key, value in self.divisible_by.items():
            self.divisible_by[key] = (self.divisible_by[key] + add_value) % key

    def update_divisible_by_on_multiply(self, multiply_value):
        for key, value in self.divisible_by.items():
            self.divisible_by[key] = (self.divisible_by[key] * multiply_value) % key

    def update_divisible_by_on_square(self):
        for key, value in self.divisible_by.items():
            self.divisible_by[key] = (self.divisible_by[key] * self.divisible_by[key]) % key

class Monkey:
    name = None
    items = None
    operation = None
    throw_test = 0
    true_target = None
    false_target = None
    inspect_count = 0
    send_indices = list[int]

    def __init__(self, name):
        self.name = str(name)
        self.items = []

    def get_inspect_count(self):
        return self.inspect_count

    def get_name(self):
        return self.name

    def add_item(self, item):
        self.items.append(item)

    def set_operation(self, op):
        self.operation = op.split("=")[1].strip()

    def set_test(self, test_condition):
        self.throw_test = test_condition

    def set_targets(self, true_target, false_target):
        self.true_target = true_target
        self.false_target = false_target

    def process_operation(self, item):
        temp = self.operation
        val = item.get_value()
        temp = temp.replace("old", "val")
        result = eval(temp)
        return int(result)
    
    def update_items(self):
        if "+" in self.operation:
            for item in self.items:
                item.update_divisible_by_on_add(int(self.operation.split()[-1]))
        elif self.operation == "old * old":
            for item in self.items:
                item.update_divisible_by_on_square()
        else:
            for item in self.items:
                item.update_divisible_by_on_multiply(int(self.operation.split()[-1]))

        self.inspect_count += len(self.items)

    def execute(self, worry_reduction_factor):
        global monkeys

        # Inspect each item
        for item_worry_level in self.items:
            self.inspect_count += 1
            # Process worry level
            item_worry_level = self.process_operation(item_worry_level)

            # Reduce worry level
            item_worry_level = Item(int(item_worry_level) // int(worry_reduction_factor))

            # Test and throw
            if item_worry_level.get_value() % self.throw_test == 0:
                monkeys[str(self.true_target)].add_item(item_worry_level)
            else:
                monkeys[str(self.false_target)].add_item(item_worry_level)
        self.items.clear()


    def get_monkeys_to_send(self):
        send_on_true_list = [item for item in self.items if item.divisible_by[self.throw_test] == 0]
        send_on_false_list = [item for item in self.items if item.divisible_by[self.throw_test] != 0]
        self.items = []
        return {self.send_indices[0]: send_on_true_list,
                self.send_indices[1]: send_on_false_list}

    def receive_items(self, items_to_receive: list[Item]):
        self.items.extend(items_to_receive)

    def get_description(self):
        return f"Monkey {self.name}:\n  Starting items: {self.items}\n  Operation: {self.operation}\n \
 Test: divisible by {self.throw_test}\n    If true: throw to monkey {self.true_target}\n \
   If false: throw to monkey {self.false_target}\n\n"

    def get_item_description(self):
        return f"Monkey {self.name}: {self.items}"

    def __str__(self):
        return f"Monkey {self.name} inspected items {self.inspect_count} times."

def process_input(raw_input: str):
    global monkeys
    monkeys.clear()
    monkey = None
    true_target = None
    false_target = None
    for line in raw_input:
        line = line.strip()
        if len(line) == 0 and monkey is not None:
            pass
        elif line.startswith("Monkey"):
            temp = line.replace(":","").split(" ")
            monkey = Monkey(temp[1])
        elif line.startswith("Starting"):
            temp = line.split(":")
            items = temp[1].split(",")
            for item in items:
                monkey.add_item(Item(int(item)))
        elif line.startswith("Operation"):
            temp = line.split(":")
            monkey.set_operation(temp[1])
        elif line.startswith("Test"):
            temp = line.split(":")
            divisor = int(temp[1][temp[1].rindex(" "):])
            monkey.set_test(divisor)
        elif line.startswith("If true:"):
            true_target = int(line[line.rindex(" "):])
            current_send_indices =[true_target]
        elif line.startswith("If false:"):
            false_target = int(line[line.rindex(" "):])
            current_send_indices.append(false_target)
            monkey.set_targets(true_target, false_target)
            monkey.send_indices = current_send_indices
            monkeys[monkey.get_name()] = monkey
    
def part_1():
    global monkeys

    for round in range(0, 20):
        for monkey in monkeys:
            monkeys[monkey].execute(3)

    counts = []
    for monkey in monkeys:
        print(monkeys[monkey])
        counts.append(monkeys[monkey].get_inspect_count())

    counts.sort(reverse = True)
    
    return counts[0] * counts[1]

def simulate_cycle(monkey_list: list[Monkey]):
    global monkeys

    for monkey in monkeys:
        monkeys[monkey].update_items()
        dict_to_send = monkeys[monkey].get_monkeys_to_send()
        for key in dict_to_send.keys():
            monkeys[str(key)].receive_items(dict_to_send[key])
    return monkeys

def part_2():
    global monkeys

    for _ in tqdm(range(10000)):
        monkeys = simulate_cycle(monkeys)
    temp = sorted([monkeys[monkey].inspect_count for monkey in monkeys])[-2:]
    return temp[0] * temp[1]

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as puzzle_input:
        raw_input = puzzle_input.readlines()

    max_cycle = process_input(raw_input)
    ans1 = part_1()
    print(f"{ans1}")
    max_cycle = process_input(raw_input)
    ans2 = part_2()
    print(ans2)