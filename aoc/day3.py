import util


class SledMap:
    def __init__(self, fp: str):
        with open(fp) as f:
            self.grid = [x.strip() for x in f.readlines()]
        self.max_x = len(self.grid[0])
        self.max_y = len(self.grid)

    def content(self, x: int, y: int) -> str:
        return self.grid[y][x % self.max_x]

    def is_tree(self, x: int, y: int) -> bool:
        return self.content(x, y) == "#"

    def traverse_a(self, x_increment: int = 3, y_increment: int = 1, output=True):
        x = 0
        y = 0
        trees = 0

        while y + 1 < self.max_y:
            x += x_increment
            y += y_increment
            if self.is_tree(x, y):
                trees += 1

        if output:
            print(
                f"Traversal: [pattern=({x_increment}, {y_increment}), result={trees}]"
            )

        return trees


if __name__ == "__main__":
    sled_map = SledMap(util.get_input_path("day3_1.txt"))
    result = sled_map.traverse_a(1, 1)
    result = result * sled_map.traverse_a(3, 1)
    result = result * sled_map.traverse_a(5, 1)
    result = result * sled_map.traverse_a(7, 1)
    result = result * sled_map.traverse_a(1, 2)
    print(result)
